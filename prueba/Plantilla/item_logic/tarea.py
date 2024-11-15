from item_logic.crud_inheritance.tarea_crud import TareaCrud
from fastapi.encoders import jsonable_encoder

crud = TareaCrud()

#Post
async def post(input):
    result = await crud.create_item(input)
    return result

#Put
async def put(id,data):
    result = await crud.update_id(id,data)
    return result

#Get complejo
async def get(filter):
    results = []
    if len(filter)>0:
        results = await crud.get_by_filter(filter)
    else:
        results = await crud.get_collection()
    return results

# Get por id
async def get_by_id(id):
    result = await crud.get_id(id)
    return result

#Delete
async def delete(id):
    deleted = await crud.delete_id(id)
    return deleted
