import streamlit as st
from critics.text import text 
def critic_text():
    st.header('Critic Text')
    col1, col2 = st.columns([3, 2])
    with col1:
        long_story = st.text_area('Story:',height=700,value=st.session_state['long_form_story'])
    with col2:
        with st.container():
            st.header("Text Critic")
            refine_sent = st.text_area('Input Sentence:', height=20)
            if st.button("Text Critique", key='text_critic'):

                Text=text.Refinement(refine_sent)
                final_refinement=Text.Two_refinement()
                voice=st.text_area("First Critique", height=20,value=final_refinement['voice'])
                image=st.text_area("Second Critique", height=20, value=final_refinement['image'])
                select=st.text_area("Second Critique", height=20, value=final_refinement['select'])
                
                