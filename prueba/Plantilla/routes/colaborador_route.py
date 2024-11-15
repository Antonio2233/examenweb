from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, List

# -----------------------------------------

from models.colaborador_schema import colaboradorSchema
import item_logic.colaborador as colaborador_logic
from models.tarea_schema import tareaSchema

# -----------------------------------------
# python -m uvicorn main:app
router = APIRouter()

@router.post("/")
async def post_(input: colaboradorSchema = Body(...)):
    try:
        result = await colaborador_logic.post(input.model_dump())
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

# @router.put("/{id}/update")
# async def put_(id: str,input: primerSchema = Body(...)):
#     try:
#         result = await primer_logic.put(id,input.model_dump())
#         return result
#     except Exception as e:
#         print(f"Failed to retrieve entry: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to update")

# @router.delete("/{id}")
# async def delete_(id: str):
#     try:
#         deleted = await primer_logic.delete(id)
#         return deleted
#     except Exception as e:
#         print(f"Failed to delete entry: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to delete")


# @router.get("/{id}")
# async def get_by_id(id: str):
#     try:
#         result = await primer_logic.get_by_id(id)
#         return result
#     except Exception as e:
#         print(f"Failed to retrieve entry: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to retrieve")

# -------------------------------- ALTERNATIVOS --------------------------------------------------


# @router.put("/{email}/update")
# async def put_by_(email: str,input: colaboradorSchema = Body(...)):
#     try:
#         result = await colaborador_logic.put_by(email,input.model_dump())
#         return result
#     except Exception as e:
#         print(f"Failed to retrieve entry: {str(e)}")
#         raise HTTPException(status_code=500, detail="Failed to update")

@router.delete("/{email}")
async def delete_by_email(email: str):
    try:
        deleted = await colaborador_logic.delete_by(email)
        return deleted
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete")

@router.get("/{email}")
async def get_by_email(email: str):
    try:
        result = await colaborador_logic.get_secundario(email)
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve")

# ------------------------------------ FIN ALTERNATIVOS -------------------------------------------

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

        usuarios = await colaborador_logic.get(filter)
        return usuarios

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Retrieve failed")



# --------------------------------------

@router.get("/{email}/habilidades")
async def get_all_habilidades(email : str):
    try:
        habilidades = await colaborador_logic.get_habilidades(email)

        return habilidades
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Get ALL habilidades failed")

@router.post("/{email}/habilidades")
async def post_habilidad(email: str,nombre: str):
    try:
        result = await colaborador_logic.post_habilidad_logic(email,nombre)

        if "message" in result and result["message"] == "Habilidad añadida.":
            return {"message": result["message"]}
        else:
            raise HTTPException(status_code=400, detail=result["message"])

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")


@router.delete("/{email}/habilidades/")
async def delete_habilidad(telefono: str,nombre: str):
    try:
        result = await colaborador_logic.delete_habilidad_logic(telefono,nombre)

        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="delete failed")

# Asignar un colaborador a una tarea, para lo cual se comprobará que el colaborador posea al menos una de las
# habilidades requeridas por la tarea.


@router.post("/{email}/tareas")
async def asignar_tarea(email: str,input: colaboradorSchema = Body(...)):
    try:
        result = await colaborador_logic.asignar(email,input.model_dump())
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")