import uvicorn
from fastapi import FastAPI, Request
from src.graph.bloggraph import BlogGraph

app=FastAPI()

@app.post('/blogs')
async def blogs(request: Request):
    data=await request.json()
    topic=data.get('topic', '')
    current_language=data.get('current_language', '')
    graph=BlogGraph().graph_builder()
    response=graph.invoke({'topic':topic, 'current_language':current_language})
    return {'response': response}
    
if __name__=="__main__":
    uvicorn.run("app:app", host='127.0.0.1', port=8001, reload=True)