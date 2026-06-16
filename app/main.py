from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="TODO API")

todos = []
counter = 1

class TodoCreate(BaseModel):
    title: str

@app.get("/todos")
def get_todos():
    return todos

@app.post("/todos")
def create_todo(todo: TodoCreate):
    global counter
    new_todo = {
        "id": counter,
        "title": todo.title
    }
    todos.append(new_todo)
    counter += 1
    return new_todo

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}
    raise HTTPException(status_code=404, detail="Todo not found")

@app.get("/health")
def health():
    return {"status": "ok"}
