import os
import re
import random
import pandas as pd
from tqdm import tqdm
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from evaluation_prompt import two_comp_plan, three_comp_plan, persona_comparision, two_comp_sent

# EvalGPT4 class handles the evaluation of two storylines using GPT-4.
class EvalGPT4:
    def __init__(self, start_index, end_index, root_dir_A, root_dir_B, criteria, api_key, evaluation_prompt):
        super().__init__()  # Call to parent class (if any) for future extensibility.
        self.start_index = start_index
        self.end_index = end_index
        self.root_dir_A = root_dir_A
        self.root_dir_B = root_dir_B
        self.criteria = criteria
        self.api_key = api_key 
        self.evaluation_prompt = evaluation_prompt

    # Set up the GPT-4 LLM with memory for conversation and evaluation
    def llm_setting(self):
        llm = ChatOpenAI(
            model='gpt-4',
            temperature=0.0,  # No creativity, for consistent evaluation
            openai_api_key=self.api_key,  
            max_tokens=512  # Limit token count
        )
        memory = ConversationBufferMemory()
        conversation = ConversationChain(
            llm=llm,
            memory=memory,
            verbose=True
        )
        return {'memory': memory, 'conversation': conversation}
    
    # Static method to read the content of a file
    @staticmethod
    def read_file_content(file_name: str):
        with open(file_name, 'r', encoding='utf-8') as file:
            return file.read().strip()
    
    # Static method to extract the winning pattern (e.g., [[A]] or [[B]])
    @staticmethod
    def find_winning_pattern(input_string):
        pattern = r'\[\[.*?\]\]'
        matches = re.findall(pattern, input_string)
        result = [i.replace('[[', '').replace(']]', '') for i in matches]
        return result

    # Method to evaluate two storylines and determine the winner
    def evaluation_two_storyline(self, result_index):
        b_critic = self.read_file_content(os.path.join(self.root_dir_B, f'{result_index}.txt'))
        a_critic = self.read_file_content(os.path.join(self.root_dir_A, f'{result_index}.txt'))

        random_integer = random.randint(0, 1)
        if random_integer == 0:
            eval_prompt = self.evaluation_prompt.format(storyline_A=b_critic, storyline_B=a_critic)
        else: 
            eval_prompt = self.evaluation_prompt.format(storyline_A=a_critic, storyline_B=b_critic)

        # Keep generating responses until a valid win list of length 4 is found
        while True:
            util = self.llm_setting()
            conversation = util['conversation']
            conversation.predict(input=eval_prompt)
            saved_dict = conversation.memory.chat_memory.dict()
            output = str(saved_dict['messages'][1]['content'])
            win_list = self.find_winning_pattern(output)
            if len(win_list) == 4:
                break

        # Adjust the result if the random integer flipped the storyline positions
        if random_integer == 1:
            win_list = ['B' if x == 'A' else 'A' if x == 'B' else x for x in win_list]
        return win_list

    # Evaluate two storylines based on personas
    def evaluation_persona(self, result_index):
        evaluation_prompt = persona_comparision
        b_critic = self.read_file_content(os.path.join(self.root_dir_B, f'{result_index}.txt'))
        a_critic = self.read_file_content(os.path.join(self.root_dir_A, f'{result_index}.txt'))

        random_integer = random.randint(0, 1)
        if random_integer == 0:
            eval_prompt = evaluation_prompt.format(storyline_A=b_critic, storyline_B=a_critic)
        else: 
            eval_prompt = evaluation_prompt.format(storyline_A=a_critic, storyline_B=b_critic)

        # Keep generating responses until a valid win list of length 4 is found
        while True:
            util = self.llm_setting()
            conversation = util['conversation']
            conversation.predict(input=eval_prompt)
            saved_dict = conversation.memory.chat_memory.dict()
            output = str(saved_dict['messages'][1]['content'])
            win_list = self.find_winning_pattern(output)
            if len(win_list) == 4:
                break
        
        # Adjust the result if random_integer flipped the storylines
        if random_integer == 1:
            win_list = ['B' if x == 'A' else 'A' if x == 'B' else x for x in win_list]
        return win_list

    # Evaluate storylines using multiple iterations
    def evaluation_iteration(self, result_index):
        b_critic = self.read_file_content(os.path.join(self.root_dir_B, f'{result_index}.txt'))
        a_critic = self.read_file_content(os.path.join(self.root_dir_A, f'{result_index}.txt'))

        # Read the iteration comparison plan
        evaluation_prompt = three_comp_plan
        iter_path = self.read_file_content(os.path.join(self.root_dir_A, f'{result_index}.txt'))
        iter_li = iter_path.split('================')
        
        iter_li.pop(0)
        iter_list = []
        for indx, i in enumerate(iter_li):
            spliii = i.split('Outline')
            iter_list.append(spliii[-1])

        random_integer = random.randint(0, 2)
        index_num = [-1, -2, 0, 1, 2]
        selected_indexes = []
        for _ in range(5):
            selected_index = random.choice(index_num)
            selected_indexes.append(selected_index)
            index_num.remove(selected_index)

        # Select storylines based on indexes
        storyline_A = iter_list[selected_indexes[0]]
        storyline_B = iter_list[selected_indexes[1]]
        storyline_C = iter_list[selected_indexes[2]]
        storyline_D = iter_list[selected_indexes[3]]
        storyline_E = iter_list[selected_indexes[4]]

        eval_prompt = three_comp_plan.format(storyline_A={storyline_A}, storyline_B={storyline_B},storyline_C={storyline_C}, storyline_D={storyline_D},storyline_E={storyline_E})

        # Keep generating responses until a valid win list of length 3 is found
        while True:
            util = self.llm_setting()
            conversation = util['conversation']
            conversation.predict(input=eval_prompt)
            saved_dict = conversation.memory.chat_memory.dict()
            output = str(saved_dict['messages'][1]['content'])
            win_list = self.find_winning_pattern(output)
            if len(win_list) == 3:
                break

        index_to_win = {-1: 'E', -2: 'D', 0: 'A', 1: 'B', 2: 'C'}
        new_list = []
        restored_win_list = []
        
        for selected_index in selected_indexes:
            new_list.append(index_to_win[selected_index])
    
        mapping2 = {0: 'A', 1: 'B', 2: 'C', 3:'D', 4:'E'}
        
        for win in win_list:
            if win == 'TI':
                restored_win_list.append('TI')
            else:
                changed_win = mapping2[new_list.index(win)]
                restored_win_list.append(changed_win)
        return restored_win_list

    # Iterate over multiple evaluations and return a DataFrame with results
    def iter_result(self):
        columns = ['Interesting', 'Coherence', 'Creative']
        df = pd.DataFrame(columns=columns)
        for index in range(self.start_index, self.end_index + 1):
            sample = self.evaluation_iteration(index)
            df.loc[index] = sample
            df.to_csv('gpt_4_evaluation_iteration_3.csv')
        return df

    # Run the evaluation and save results to a CSV file
    def eval_result(self, output_file):
        df = pd.DataFrame(columns=self.criteria)
        for index in tqdm(range(self.start_index, self.end_index + 1), desc="Evaluating"):
            sample = self.evaluation_two_storyline(index)
            df.loc[index] = sample
            df.to_csv(output_file, index=False)
        return df

    # Evaluate personas and save results to a CSV file
    def eval_persona_result(self):
        columns = ['Interesting', 'Coherence', 'Creative', 'Closer']
        df = pd.DataFrame(columns=columns)
        for index in range(self.start_index, self.end_index + 1):
            sample = self.evaluation_persona(index)
            df.loc[index] = sample
            df.to_csv('gpt_4_evaluation_persona_result.csv')
        return df 


if __name__ == "__main__":
    import argparse

    # Command-line arguments parsing
    parser = argparse.ArgumentParser(description="Evaluation script using GPT-4")
    parser.add_argument("start_index", type=int, help="Evaluation start index")
    parser.add_argument("end_index", type=int, help="Evaluation end index")
    parser.add_argument("root_dir_A", type=str, help="Directory path for Story A")
    parser.add_argument("root_dir_B", type=str, help="Directory path for Story B")
    parser.add_argument("criteria", type=str, help="Evaluation criteria, comma separated (e.g. Interesting,Coherence,Creative,Closer)")
    parser.add_argument("api_key", type=str, help="OpenAI API Key")
    
    args = parser.parse_args()

    # Initialize the parameters
    start_index = args.start_index
    end_index = args.end_index
    root_dir_A = args.root_dir_A
    root_dir_B = args.root_dir_B
    criteria = args.criteria.split(',')  
    api_key = args.api_key
    evaluation_prompt = two_comp_sent

    output_file = 'gpt_4_evaluation_result.csv'
    
    # Create an evaluation instance
    evaluation = EvalGPT4(
        start_index=start_index, 
        end_index=end_index, 
        root_dir_A=root_dir_A, 
        root_dir_B=root_dir_B, 
        criteria=criteria, 
        api_key=api_key, 
        evaluation_prompt=evaluation_prompt
    )
    
    # Run the evaluation
    evaluation.eval_result(output_file)
