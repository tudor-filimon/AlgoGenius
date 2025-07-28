import os
from dotenv import load_dotenv
from autogen_agentchat.openai import OpenAIChatCompletionClient
from config.constants import MODEL

load_dotenv()
api_key= os.getenv('OPEN_AI_KEY')

def get_model_client():
    model_client = OpenAIChatCompletionClient(model=MODEL, api_key=api_key)
    return model_client