from item_logic.crud_inheritance.evento_crud import EventoCrud
from fastapi.encoders import jsonable_encoder

crud = EventoCrud()

#Post
async def post(input):
    data = jsonable_encoder(input)
    result = await crud.create_item(data)
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


async def invitar(id,email):
    result = await crud.add_invitado(id,email)
    return result


async def aceptar(id,email):
    result = await crud.aceptar(id,email)
    return result


async def reprogramar(id,year,month,day):
    result = await crud.reprogramar(id,year,month,day)
    return result