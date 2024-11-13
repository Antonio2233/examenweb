from item_logic.crud_inheritance.usuario_crud import UsuarioCrud
from fastapi.encoders import jsonable_encoder

crud = UsuarioCrud()

#Post
async def post_usuario(user):
    # user_data = jsonable_encoder(user)
    result = await crud.create_item(user)
    return result

#Get complejo
async def get_usuarios(filter):
    users = []
    if len(filter)>0:
        users = await crud.get_by_filter(filter)
    else:
        users = await crud.get_collection()
    return users

#Get complejo
async def get_user(email):
        filter = {}
        filter["email"] = {"$regex": ".*{}.*".format(email), "$options": "i"}
        user = await crud.encuentra_uno(filter)
        return user


#Delete
async def delete_user(id):
    deleted = await crud.delete_id(id)
    return deleted

#Get all simple
async def get_all_usuarios():
    users = []
    users = await crud.get_collection()
    return users

#Get all simple
async def get_all_usuarios():
    result = []
    result = await crud.get_contactos()
    return result

#Get contactos
async def get_contactos(email):
    result = await crud.get_contactos(email)

    return result


async def post_contacto(user,contacto):
    # user_data = jsonable_encoder(user)
    result = await crud.add_contact(user,contacto)

    return result

async def delete_contacto(user: str,contacto: str):
    result = await crud.delete_contact(user,contacto)

    return result


#QUERIE1
async def querie_contactos_dupla(email: str, nombrecontacto: str):
    result = await crud.get_contactos_dupla(email,nombrecontacto)

    return result


# QUERIE2
