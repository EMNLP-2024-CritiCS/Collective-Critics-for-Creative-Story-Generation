from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from critics.setting.promptDesign import story_template  
from critics.setting.chatsetting.gptsetting import chatsettubg  
from critics.setting.util import write_to_file 
import random
import logging
import datetime
import re
import yaml
import string
import argparse
import os
import pandas as pd

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Get the current time
current_time = datetime.datetime.now()

# A divider bar for formatting outputs
divide_bar = '=' * 180

# Refinement class: Handles refinement tasks for both image and voice aspects of a story
class Refinement:
    def __init__(self, sentence):
        super().__init__()
        self.sentence = sentence
        
    # Refine the story with a focus on imagery
    def image_refinmenet(self) -> str:
        refine_prompt = story_template.refine_prompt_image.format(story=self.sentence)
        util = chatsettubg()
        conversation = util['conversation']        
        conversation.predict(input=refine_prompt)
        
        # Extract the conversation's memory and output (refinement suggestions)
        saved_dict = conversation.memory.chat_memory.dict()
        five_refi = str(saved_dict['messages'][1]['content'])
        
        return five_refi
    
    # Refine the story with a focus on voice 
    def voice_refinement(self) -> str:
        refine_prompt = story_template.refine_prompt_voice.format(story=self.sentence)
        
        # Set up the conversation
        util = chatsettubg()
        conversation = util['conversation']
        conversation.predict(input=refine_prompt)
        
        saved_dict = conversation.memory.chat_memory.dict()
        five_refi = str(saved_dict['messages'][1]['content'])
        
        return five_refi
    
    # This function takes the results from image and voice refinement and selects the best one
    def leader(self, voice, image) -> str:
        select_three_prompt = story_template.choose_critic.format(Image_refinement=image, Voice_refinement=voice)
        util = chatsettubg()
        conversation = util['conversation']
        
        conversation.predict(input=select_three_prompt)
        
        saved_dict = conversation.memory.chat_memory.dict()
        three_refine = str(saved_dict['messages'][1]['content'])
        
        return three_refine
    
    # Split persona content into individual personas
    def split_personas(self):
        def extract_section(text, start_pattern, end_pattern):
            pattern = rf"{start_pattern}(.*?){end_pattern}"
            matches = re.findall(pattern, text, re.DOTALL)
            return matches[0].strip() if matches else ""
        
        first_persona = extract_section(persona, r'Expert 1.', r'Expert 2.')
        second_persona = extract_section(persona, r'Expert 2.', r'Leader.')
        leader_persona = extract_section(persona, r'Leader.', r'\Z')
        
        return {
            "first_persona": first_persona,
            "second_persona": second_persona,
            "leader": leader_persona
        }
    
    # Perform both image and voice refinement and return the results
    def Two_refinement(self) -> dict:
        image = self.image_refinmenet()
        voice = self.voice_refinement()
        
        select = self.leader(voice=voice, image=image)
        
        final_refinement = {'voice': voice, 'image': image, 'select': select}
        
        return final_refinement
