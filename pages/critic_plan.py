import streamlit as st
from pages.utils import JsonToPlan, StoryParser, extract_section
from critics.plan import plan 
    
def plan_tab_creator(tab_names):
    tabs = st.tabs(tab_names)
    for tab, name in zip(tabs, tab_names):
        with tab:
            st.header(name)
            premise = st.text_area("Premise:", height=20, value=st.session_state['premise'], key=name+'_premise')
            setting = st.text_area("Setting:", height=20, value=st.session_state['setting'][name],key=name+'_setting')
            characters = st.text_area("Characters:", height=20, value=st.session_state['characters'][name],key=name+'_characters')
            outline = st.text_area("Outline:", height=500, value=st.session_state['outline'][name],key=name+'_outline')

def critic_plan():
    st.header('Critic Plan')
    title = 'Create Plan'
    plan_index = 0
    json_path = 'scripts/output/plan.json'
    formatter = JsonToPlan(json_path)
    outline_text_path = f'pages/db/story_plan/{plan_index}.txt'
    plan_dict = formatter.save_to_file(outline_text_path)
    formated_text = formatter.create_formatted_text()


    if 'setting' not in st.session_state:
        st.session_state['setting'] = {'Plan_1' : plan_dict['setting']}
    if 'characters' not in st.session_state:
        st.session_state['characters'] = {'Plan_1' : plan_dict['characters']}
    if 'outline' not in st.session_state:
        st.session_state['outline'] = {'Plan_1' : plan_dict['outline']}        
        st.session_state['plan_list'] = ['Plan_1']
    if 'storyline' not in st.session_state:
        st.session_state['storyline'] = formated_text
        st.session_state['storyline_list'] = [formated_text]

    col1, col2, col3 = st.columns([3, 2,1])
    with col1:
        plan_tab_creator(st.session_state['plan_list'])
        
    with col2:
        with st.container():
            st.header("Plan Critic")
            select_critique = st.session_state.get('critic_list', {}).get('inspector', '')
            if st.button('Plan Critique', key='critic_plan'):
                plan_ix = len(st.session_state['plan_list']) + 1
                Critic=plan.Critic(formated_text)
                st.session_state['critic_list']=Critic.three_critic()
                first_critique = st.text_area("First Critique", height=20, value=st.session_state.get('critic_list', {}).get('sturcture', ''))
                second_critique = st.text_area("Second Critique", height=20, value = st.session_state.get('critic_list', {}).get('ending', ''))
                third_critique = st.text_area("Third Critique", height=20, value = st.session_state.get('critic_list', {}).get('original',''))
                select_critique = st.text_area('Selected Critique', height=20)
                
                
            if st.button("Refine Plan", key='refine_plan'):
                plan_ix = len(st.session_state['plan_list']) + 1
                print(select_critique)
                refined_plan=plan.modifiedStoryline(st.session_state['storyline'], select_critique)
                st.session_state['setting'][f'Plan_{plan_ix}'] = extract_section(refined_plan, 'Setting','Characters')
                st.session_state['characters'][f'Plan_{plan_ix}'] = extract_section(refined_plan, 'Characters','Outline')
                st.session_state['outline'][f'Plan_{plan_ix}'] = extract_section(refined_plan, 'Outline',r"\Z")
                st.session_state['plan_list'].append(f'Plan_{plan_ix}')
                st.session_state['storyline_list'].append(refined_plan)
                st.experimental_rerun()
    with col3:
        final_list=list(st.session_state['plan_list'])
        final_list.append('AutoSelect')
        final_plan = st.radio("Final_Plan", final_list)
        if st.button("Final Plan", key='final_plan'):
            if final_plan == 'AutoSelect':
                evalGPT=plan.Story_Selector(st.session_state['storyline_list'])
                eval_result=evalGPT.final_select()
                
                st.session_state['final_setting']= extract_section(eval_result, 'Setting','Characters')
                st.session_state['final_characters']=extract_section(eval_result, 'Characters','Outline')
                st.session_state['final_outline']=extract_section(eval_result, 'Outline',r"\Z")
            else:
                st.session_state['final_setting']=st.session_state['setting'][final_plan]
                st.session_state['final_characters']=st.session_state['characters'][final_plan]
                st.session_state['final_outline']=st.session_state['outline'][final_plan]
            
            st.session_state['current_page'] = 'create_story'
            st.experimental_rerun()
    col1, col2 = st.columns([3, 2])