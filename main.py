from fastapi import FastAPI
from model import Todo
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos=[]
# get all todo
@app.get('/todos')
async def get_todos():
    return { 'todo': todos }
# get single todo
# create new todo
@app.post('/todos')
async def create_todos(todo:Todo):
    todos.append(todo)
    return { 'message': "new todo added" }
# update existing todo
# delete a todo