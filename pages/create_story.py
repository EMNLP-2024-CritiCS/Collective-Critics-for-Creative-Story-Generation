import streamlit as st
from pages.utils import StoryParser
import subprocess, json
import pandas as pd
import os 

def create_story():
    final_premise = st.text_area("Premise:", height=20, value=st.session_state['premise'])
    final_setting = st.text_area("Setting:", height=20, value=st.session_state['final_setting'])
    final_characters = st.text_area("Characters:", height=20, value=st.session_state['final_characters'])
    final_outline = st.text_area("Outline:", height=500, value=st.session_state['final_outline'])
    
    format_string = 'Premise ' + st.session_state['premise'] + '\n\n' + 'Setting '+ st.session_state['final_setting'] + '\n\n' + 'Characters:'+'\n'+st.session_state['final_characters']+'\n'+'Outline:'+'\n'+st.session_state['final_outline']
    
    directory = os.path.dirname('pages/db/story_plan/txt/final_plan.txt')
    if not os.path.exists(directory):
        os.makedirs(directory)
        
    with open('pages/db/story_plan/txt/final_plan.txt', 'w', encoding='utf-8') as file:
        file.write(format_string)
    
    if st.button("Generate Long Story", key='long_story'):
        parser=StoryParser('pages/db/story_plan/txt/final_plan.txt')
        story_parser=parser.convert_to_json()
        
        json_file_path = 'scripts/output/final_plan.json'
        json_directory = os.path.dirname(json_file_path)

        if not os.path.exists(json_directory):
            os.makedirs(json_directory)

        with open(json_file_path, 'w', encoding='utf-8') as plan_json:
            plan_json.write(story_parser)
        # subprocess.run(['python', 'scripts/story/generate.py'], capture_output=True, text=True)    

        
        # if 'long_form_story' not in st.session_state:
        #     file_path = 'scripts/output/story.txt'
        #     directory = os.path.dirname(file_path)
            
        #     if not os.path.exists(directory):
        #         os.makedirs(directory)

        #     if os.path.exists(file_path):
        #         with open(file_path, 'r', encoding='utf-8') as file:
        #             long_story = file.read()
        #         st.session_state['long_form_story'] = long_story
        #         st.session_state['current_page'] = 'critic_text'
        #         st.experimental_rerun()
        #     else:
        #         st.error(f"File not found: {file_path}")
    