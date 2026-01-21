import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self):
        load_dotenv()
        
    def groqllm(self):
        try:
            # os.environ['GROQ_API_KEY']=
            groq_api_key=os.getenv('GROQ_API_KEY')
            self.llm=ChatGroq(api_key=groq_api_key, model='llama-3.1-8b-instant')
            return self.llm
        except Exception as e:
            raise ValueError(e)