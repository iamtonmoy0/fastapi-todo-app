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
@app.get('/todos/{item_id}')
async def get_single_todos(item_id:int):
    for todo in todos:
        if todo.id==item_id:
            return {"todo",todo}
	return {"message":"no todo found"}
# create new todo
@app.post('/todos')
async def create_todos(todo:Todo):
    todos.append(todo)
    return { 'message': "new todo added" }
# update existing todo

# delete a todo
@app.delete('/todos/{item_id}')
async def delete_todos(item_id:int):
    for todo in todos:
        if todo.id==item_id:
            todos.remove(todo)
            
	return {"message":"no todo found"}