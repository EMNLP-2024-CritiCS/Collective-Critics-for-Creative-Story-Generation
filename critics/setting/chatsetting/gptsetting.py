# Import necessary modules
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain_openai import OpenAI  
import os

# Fetch the OpenAI API key from the environment variables
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# Function to set up the chat model and conversation chain
def chatsettubg(model_name='gpt-3.5-turbo', stop=None, completion=None):
    if completion == 'completion_mode':
        llm = OpenAI(
            model='gpt-3.5-turbo-instruct', 
            temperature=1.0,                 
            max_tokens=1400,                 
            openai_api_key=OPENAI_API_KEY,  
            stop=stop                       
        )
        return llm  

    if stop is not None:
        llm = ChatOpenAI(
            model=model_name,                # Model to use (e.g., 'gpt-3.5-turbo', 'gpt-4')
            temperature=1.0,                 # Temperature
            openai_api_key=OPENAI_API_KEY,   # API key 
            stop=stop                        # Stop sequence 
        )
    else:
        # Default case: No stop sequence provided
        llm = ChatOpenAI(
            model=model_name,                # Default model
            temperature=1.0,                 # Default temperature for balanced creativity
            openai_api_key=OPENAI_API_KEY    # API key for authentication
        )
    
    memory = ConversationBufferMemory()
    
    conversation = ConversationChain(
        llm=llm,                          
        memory=memory,                      
        verbose=True                       s
    )
    
    # Return a dictionary with the memory and conversation chain for further use
    return {'memory': memory, 'conversation': conversation}
