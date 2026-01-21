from langgraph.graph import StateGraph, START, END
from src.state.blogstate import BlogState
from src.nodes.graphnodes import GraphNodes
from src.llms.groqllm import GroqLLM

class BlogGraph:
    def __init__(self):
        self.llm=GroqLLM().groqllm()
        
    def graph_builder(self):
        self.bloggraph=StateGraph(BlogState)
        self.nodes=GraphNodes(self.llm)
        self.bloggraph.add_node('topic_creation', self.nodes.topic_creation)
        self.bloggraph.add_node('content_creation', self.nodes.content_creation)
        self.bloggraph.add_node('hindi_translation', self.nodes.hindi_translation)
        self.bloggraph.add_node('french_translation', self.nodes.french_translation)
        
        self.bloggraph.add_edge(START, 'topic_creation')
        self.bloggraph.add_edge('topic_creation', 'content_creation')
        self.bloggraph.add_conditional_edges('content_creation', self.nodes.translation_router, {'hindi_translation':'hindi_translation', 'french_translation' : 'french_translation'})
        self.bloggraph.add_edge('hindi_translation', END)
        self.bloggraph.add_edge('french_translation', END)
        
        self.bloggraph_builder=self.bloggraph.compile()
        
        return self.bloggraph_builder