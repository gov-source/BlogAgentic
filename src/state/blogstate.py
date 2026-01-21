from typing import TypedDict
from pydantic import BaseModel, Field

class Blog(BaseModel):
    title: str= Field(description="This contain the topic in one line")
    content: str= Field(description="This contains the brief summary about the topic in less than 100 words")
    
class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str