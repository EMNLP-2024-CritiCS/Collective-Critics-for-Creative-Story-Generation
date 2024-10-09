import random
import logging
import datetime
import re
import yaml
import string
import argparse
import os
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from critics.setting.promptDesign import storyline_template, critic_persona
from critics.setting.chatsetting.gptsetting import chatsettubg
from critics.setting.util import write_to_file

# Get the current time
current_time = datetime.datetime.now()
# Divider bar for formatting
divide_bar = '=' * 180

class Critic:
    def __init__(self, storyline):
        super().__init__()
        self.storyline = storyline

    # Critique the story structure
    def story_structure_question(self, persona_type=None) -> str:
        storyline = self.storyline
        insert_persona = critic_persona.story_sturcture.format(second_persona=persona_type)
        critic_prompt = insert_persona + storyline + '\n' + divide_bar + '\n' + storyline_template.critic_prompt.format(critic_type=storyline_template.critieria_u_structure)

        util = chatsettubg(stop=['<question/>'])
        conversation = util['conversation']
        conversation.predict(input=critic_prompt)  
        saved_dict = conversation.memory.chat_memory.dict()  
        output = str(saved_dict['messages'][1]['content'])  
        
        # Save the result to a file
        original_setting = 'output/same_criteria/question/structure.txt'
        write_to_file(original_setting, output)
        return output

    # Critique the story ending
    def ending_question(self, persona_type=None) -> str:
        storyline = self.storyline
        insert_persona = critic_persona.ending.format(third_persona=persona_type)
        # Generate the critique prompt for story ending
        critic_prompt = insert_persona + storyline + '\n' + divide_bar + '\n' + storyline_template.critic_prompt.format(critic_type=storyline_template.critieria_u_ending)

        util2 = chatsettubg(stop=['<question/>'])
        conversation = util2['conversation']  
        conversation.predict(input=critic_prompt)
        saved_dict = conversation.memory.chat_memory.dict()
        output = str(saved_dict['messages'][1]['content'])  
        
        # Save the result to a file
        original_setting = 'output/same_criteria/question/ending.txt'
        write_to_file(original_setting, output)
        return output
    
    # Critique the originality of the story
    def original_question(self, persona_type=None) -> str:
        storyline = self.storyline
        insert_persona = critic_persona.original.format(first_persona=persona_type)
        critic_prompt = insert_persona + storyline + '\n' + divide_bar + '\n' + storyline_template.critic_prompt.format(critic_type=storyline_template.critieria_originaltiy)
        
        util3 = chatsettubg(stop=['<question/>'])
        conversation = util3['conversation']   
        conversation.predict(input=critic_prompt)
        saved_dict = conversation.memory.chat_memory.dict()
        output = str(saved_dict['messages'][1]['content']) 
        
        # Save the result to a file
        original_setting = 'output/same_criteria/question/original.txt'
        write_to_file(original_setting, output)
        return output

    # Combine all critiques and generate a final, more comprehensive critique
    def inspector_gpt(self, persona_type=None, first_critique=None, second_critique=None, third_critique=None) -> str:
        def question_indexing(critique):
            search_str = "Question"
            start_index = critique.find(search_str)
            if start_index != -1:
                return critique[start_index + len(search_str):]

        # Extract the question portion from each critique
        question_1 = question_indexing(first_critique)
        question_2 = question_indexing(second_critique)
        question_3 = question_indexing(third_critique)
        
        # Combine all critiques into a single prompt for final review
        lu_data = self.storyline
        prompt = storyline_template.inspector_prompt.format(
            first_critique=question_1, 
            second_critique=question_2, 
            third_critique=question_3, 
            storyline=lu_data,
        )
        
        insert_persona = critic_persona.gpt_inspector.format(leader=persona_type)
        critic_prompt = insert_persona + '\n' + divide_bar + '\n' + prompt
        
        # Function to extract the final question from the model's output
        def find_result_questions(input_string):
            pattern = r"(Question|question)(.*?)(\n|$)"
            matches = re.findall(pattern, input_string)
            output = [f"Question: {match[1].strip()}" for match in matches]
            return output[0]
    
        util = chatsettubg(stop=['<answer/>'])
        conversation = util['conversation']
        conversation.predict(input=critic_prompt)
        saved_dict = conversation.memory.chat_memory.dict()
        output = str(saved_dict['messages'][1]['content'])
        output = find_result_questions(output)  
        
        # Save the final critique to a file
        original_setting = 'output/same_criteria/question/leader.txt'
        write_to_file(original_setting, output)
        return output
    
    # Split the persona content into individual persona segments
    def split_personas(self, persona):
        def extract_section(text, start_pattern, end_pattern):
            pattern = rf"{start_pattern}(.*?){end_pattern}"
            matches = re.findall(pattern, text, re.DOTALL)
            return matches[0].strip() if matches else ""
        
        first_persona = extract_section(persona, r'Expert 1', r'2')
        second_persona = extract_section(persona, r'Expert 2', r'3')
        third_persona = extract_section(persona, r'Expert 3', r'Leader')
        leader_persona = extract_section(persona, r'Leader', r'\Z')
        
        return {
            "first_persona": first_persona,
            "second_persona": second_persona,
            "third_persona": third_persona,
            "leader": leader_persona
        }
    
    # Generate critiques from three experts and a leader persona
    def three_critic(self) -> dict:
        storyline = self.storyline
        three_editer_one_leader = storyline_template.persona_creator.format(storyline=storyline)
        
        util = chatsettubg(stop=['<persona/>'])
        conversation = util['conversation']
        conversation.predict(input=three_editer_one_leader)
        save_dict = conversation.memory.chat_memory.dict()
        persona_list = save_dict['messages'][1]['content']

        persona_logging_path = 'output/persona.txt'
        write_to_file(persona_logging_path, persona_list)
        
        persona_set = self.split_personas(persona_list)
        first_persona = persona_set['first_persona']
        second_persona = persona_set['second_persona']
        third_persona = persona_set['third_persona']
        leader = persona_set['leader']

        story_structure_question = self.story_structure_question(first_persona)
        ending_question = self.ending_question(second_persona)
        original_question = self.original_question(third_persona)
        inspector_critic = self.inspector_gpt(
            persona_type=leader, 
            first_critique=story_structure_question, 
            second_critique=ending_question, 
            third_critique=original_question
        )
        
        # Combine all critiques into a final dictionary
        final_critic = {
            'structure': story_structure_question, 
            'ending': ending_question, 
            'original': original_question, 
            'inspector': inspector_critic
        }
        
        return final_critic

class Story_Selector:
    def __init__(self, story_list):
        super().__init__()
        self.story_list = story_list
        self.winning_set = []

    # Find the winning pattern (which story is the best) 
    @staticmethod
    def find_winning_pattern(input_string):
        pattern = r'\[\[.*?\]\]'
        matches = re.findall(pattern, input_string)
        result = []
        for i in matches:
            answer = i.replace('[[', '').replace(']]', '')
            result.append(answer)
        return result
    
    # Calculate the score for each story and find the winning story
    def calculateSelectScore(self, story_list):
        llm = ChatOpenAI(
            model='gpt-4',
            temperature=0, 
            openai_api_key=OPENAI_API_KEY,
        )
        memory = ConversationBufferMemory()
        conversation = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )
        
        UPPER_ALP = list(string.ascii_uppercase[:len(story_list)])
        
        critic_set = ''
        select_generation = ''
        score_dict = {}

        for temp, alp in enumerate(UPPER_ALP):
            score_dict[alp] = 0
            critic_set += 'Storyline ' + alp + ':\n' + story_list[temp] + '\n\n\n'
            select_generation += f'"[[{alp}]]" if storyline {alp} is better,' 

        # Create the prompt for selecting the best story
        select_storyline = storyline_template.select_storyline_result.format(
            critic_set=critic_set, 
            select_generation=select_generation
        )

        conversation.predict(input=select_storyline)
        saved_dict = conversation.memory.chat_memory.dict()
        raw_score = saved_dict['messages'][1]['content']
        raw_score_result = self.find_winning_pattern(raw_score)

        for inx, rel in enumerate(raw_score_result):
            if rel == 'TI':
                continue
            score_dict[rel] += 1
        
        score_logging_path = f'critics/plan/output/score.txt'
        write_to_file(score_logging_path, str(score_dict))
        
        max_value = max(score_dict.values())
        max_keys = [key for key, value in score_dict.items() if value == max_value]
        
        round_winning_set = []
        for key in max_keys:
            round_winning_set.append(story_list[UPPER_ALP.index(key)])
        self.winning_set = round_winning_set
        return round_winning_set
    
    # Perform final selection of the best story
    def final_select(self):
        count = 0
        while True:
            if len(self.winning_set) == 1:
                return self.winning_set[0]
            if count == 0:
                self.calculateSelectScore(story_list=self.story_list)
            elif count == 2:
                final_win_set = self.calculateSelectScore(story_list=self.winning_set)
                return final_win_set[0]
            else:
                self.calculateSelectScore(story_list=self.winning_set)
            count += 1

# Function to apply critiques and modify the storyline accordingly
def modifiedStoryline(storyline, final_critic) -> dict:
    prompt = storyline_template.applyQA
    apply_critic = prompt.format(final_critic=final_critic, storyline=storyline)  
    util = chatsettubg(stop=['<applyStoryline>'], model_name='gpt-4')
    conversation = util['conversation']
    conversation.predict(input=apply_critic)
    saved_dict = conversation.memory.chat_memory.dict()
    output = saved_dict['messages'][1]['content']
    return output
