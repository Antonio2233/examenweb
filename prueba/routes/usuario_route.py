from fastapi import APIRouter, HTTPException, Body, Query
from models.usuario_schema import usuarioSchema
import item_logic.usuario as usuario_logic
from typing import Optional, List


# -----------------------------------------

router = APIRouter()

@router.post("/")
async def add_usuario(user: usuarioSchema = Body(...)):
    try:
        result = await usuario_logic.post_usuario(user.model_dump())
        # result = await usuario_logic.post_usuario(user)
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

# @router.get("/")
# async def get_all_usuarios():
#     try:
#         usuarios = await usuario_logic.get_all_usuarios()
#         return usuarios

#     except Exception  as e:
#         print(f"Upload failed: {str(e)}")
#         raise HTTPException(status_code=500, detail="Get ALL failed")

@router.delete("/{email}")
async def delete_usuario(id: str):
    try:
        deleted_user = await usuario_logic.delete_user(id)
        return deleted_user
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete entry")

@router.get("/{email}")
async def get_user(email: str):
    try:


        user = await usuario_logic.get_user(email)
        return user
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve user")


# GET ALL
@router.get("/")
async def get_all(
    email: Optional[str] =  Query(None),
    nombre: Optional[str] = Query(None)
):
    try:
        filter = {}
        if email:
            filter["email"] = {"$regex": ".*{}.*".format(email), "$options": "i"}
        if nombre:
            filter["nombre"] = {"$regex": ".*{}.*".format(nombre), "$options": "i"}

        usuarios = await usuario_logic.get_usuarios(filter)
        return usuarios

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Retrieve failed")


# --------------------------



@router.get("/{email}/contactos")
async def get_all_contactos(email : str):
    try:

        contactos = await usuario_logic.get_contactos(email)

        return contactos
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Get ALL failed")


@router.post("/{email}/contactos")
async def post_contacto(email: str,contacto: str):
    try:
        result = await usuario_logic.post_contacto(email,contacto)

        if "message" in result and result["message"] == "Contacto añadido.":
            return {"message": result["message"]}
        else:
            raise HTTPException(status_code=400, detail=result["message"])

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

@router.delete("/{email}/contactos")
async def delete_contacto(email: str,contacto: str):
    try:
        result = await usuario_logic.delete_contacto(email,contacto)

        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="delete failed")



# ---------------------------
# queriessss

@router.get("/{email}/contactosdupla")
async def querie_contactos(email : str,nombre : str):
    try:
        contactos = await usuario_logic.querie_contactos_dupla(email,nombre)
        return contactos
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Get ALL failed")