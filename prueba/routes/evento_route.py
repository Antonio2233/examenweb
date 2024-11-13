from fastapi import APIRouter, HTTPException, Body, Query

from models.evento_schema import eventoSchema
import item_logic.evento as evento_logic
from typing import Optional, List


# -----------------------------------------

router = APIRouter()

#Post
@router.post("/")
async def post_(input: eventoSchema = Body(...)):
    try:
        result = await evento_logic.post(input)
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")


# DELETE
@router.delete("/{id}")
async def delete_(id: str):
    try:
        deleted = await evento_logic.delete(id)
        return deleted
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete")


# GET ID
@router.get("/{id}")
async def get_by_id(id: str):
    try:
        result = await evento_logic.get_by_id(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve")


# GET ALL
@router.get("/")
async def get_all(
    anfitrion: Optional[str] =  Query(None),
    descripcion: Optional[str] = Query(None)
):
    try:
        filter = {}
        if anfitrion:
            filter["anfitrion"] = {"$regex": ".*{}.*".format(anfitrion), "$options": "i"}
        if descripcion:
            filter["descripcion"] = {"$regex": ".*{}.*".format(descripcion), "$options": "i"}

        usuarios = await evento_logic.get(filter)
        return usuarios

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Retrieve failed")


@router.put("/{id}/invitados/{email}")
async def put_new_invitado(id : str,email: str):
    try:
        result = await evento_logic.invitar(id,email)
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Put failed")


@router.put("/{id}/aceptar/{email}")
async def aceptar(id : str,email: str):
    try:
        result = await evento_logic.aceptar(id,email)
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Put failed")

@router.put("/{id}/reprogramar/{email}")
async def reprogramar(id : str,
    year: Optional[int] = Query(None),
    month: Optional[int] = Query(None),
    day: Optional[int] = Query(None)):
    try:
        result = await evento_logic.reprogramar(id,year,month,day)
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Put failed")

# @router.get("/reprogramar/")

