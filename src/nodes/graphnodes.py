from src.llms.groqllm import GroqLLM
from src.state.blogstate import BlogState, Blog

class GraphNodes:
    def __init__(self, llm):
        self.llm=llm
        self.blogstate=BlogState
        
    def topic_creation(self, state:BlogState):
        response=self.llm.invoke(f"create the one line blog title based on the topic {state['topic']}")
        return {'blog':{'title':response.content}}
        
    def content_creation(self, state:BlogState):
        response=self.llm.invoke(f"create the one line content based on the topic {state['topic']}")
        return {'blog':{'title':state['blog']['title'],'content':response.content}}   
    
    def hindi_translation(self, state:BlogState):
        response=self.llm.invoke(f"convert the content {state['blog']['content']} into hindi language")
        return {'blog':{'title':state['blog']['title'],'content':response.content}}     
    
    def french_translation(self, state:BlogState):
        response=self.llm.invoke(f"convert the content {state['blog']['content']} into french language")
        return {'blog':{'title':state['blog']['title'],'content':response.content}}   
    
    def translation_router(self, state:BlogState):
        if state['current_language'].lower()=='hindi':
            return 'hindi_translation'
        elif state['current_language'].lower()=='french':
            return 'french_translation'