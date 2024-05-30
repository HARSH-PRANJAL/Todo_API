from fastapi import APIRouter
from config.db import collection
from schemas.schema import all_serial
from models.todo import Todo
from bson import ObjectId

router= APIRouter()

#get point

@router.get("/")
async def getTodo():
    allTodo = all_serial(collection.find())
    return allTodo

# post method for insertion
@router.post("/")
async def postTodo(todo:Todo):
    collection.insert_one(dict(todo))

# update method
@router.put("/{id}")
async def updateTodo(id:str, todo:Todo):
    collection.find_one_and_update({"_id":ObjectId(id)}, {"$set":dict(todo)})

# delete method
@router.delete("/{id}")
async def deleteTodo(id:str):
    collection.find_one_and_delete({"_id":ObjectId(id)})
