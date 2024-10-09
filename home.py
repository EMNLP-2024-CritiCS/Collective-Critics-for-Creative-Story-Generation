import streamlit as st
from pages import critic_plan, create_story, critic_text

import requests
import streamlit as st
import subprocess, json
import os 
create_plan_api = "http://fastapi:55100/create_plan"
PAGES = ["create_plan", "critic_plan","create_story", "critic_text"]

def create_sidebar():
    selected_style = "style='color:skyblue;'"
    default_style = "style='color:grey;'"
    style_step_1 = selected_style if st.session_state['current_page'] == 'create_plan' else default_style
    style_step_2 = selected_style if st.session_state['current_page'] == 'critic_plan' else default_style
    style_step_3 = selected_style if st.session_state['current_page'] == 'story_create' else default_style
    style_step_4 = selected_style if st.session_state['current_page'] == 'critic_text' else default_style
    st.sidebar.markdown(f"<h2 {style_step_1}>1. Create Plan</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<h2 {style_step_2}>2. Critic Plan</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<h2 {style_step_3}>3. Create Story</h2>", unsafe_allow_html=True)
    st.sidebar.markdown(f"<h2 {style_step_4}>4. Critic Text</h2>", unsafe_allow_html=True)

def create_plan():
    title = 'Create Plan'
    st.markdown(f"<h1 style='text-align: center;'>{title}</h1>", unsafe_allow_html=True)
    sub_title = 'Write a premise for a short story'
    st.markdown(f"<h2 style='text-align: center;'>{sub_title}</h2>", unsafe_allow_html=True)
    premise = st.text_area('Input your premise here', height=300)
    if st.button('Generate Story Plan', key='generate'):
        st.session_state['premise'] = premise 
        premise_dict = {
            "title": st.session_state['premise'],
            "premise": st.session_state['premise']
        }
        os.makedirs('scripts/output', exist_ok=True)
        with open('scripts/output/premise.json','w') as json_file:
            json.dump(premise_dict, json_file, indent=4)   
        subprocess.run(['python', 'scripts/plan/generate.py'], capture_output=True, text=True)
        st.session_state['current_page'] = 'critic_plan'
        st.experimental_rerun()
def main():
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'create_plan'
    create_sidebar()
    if st.session_state['current_page'] == "create_plan":
        create_plan()
    elif st.session_state['current_page'] == "critic_plan":
        critic_plan.critic_plan()
    elif st.session_state['current_page'] == "create_story":
        create_story.create_story()
    elif st.session_state['current_page'] == "critic_text":
        critic_text.critic_text()

    
if __name__ == "__main__":
    main()