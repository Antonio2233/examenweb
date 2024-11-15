from fastapi import APIRouter, HTTPException, Body, Query
from typing import Optional, List

# -----------------------------------------

from models.tarea_schema import tareaSchema
import item_logic.tarea as tarea_logic

# -----------------------------------------

router = APIRouter()

@router.post("/")
async def post_(input: tareaSchema = Body(...)):
    try:
        result = await tarea_logic.post(input.model_dump())
        return result
    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Upload failed")

@router.put("/{id}")
async def put_(id: str,input: tareaSchema = Body(...)):
    try:
        result = await tarea_logic.put(id,input.model_dump())
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to update")


@router.delete("/{id}")
async def delete_(id: str):
    try:
        deleted = await tarea_logic.delete(id)
        return deleted
    except Exception as e:
        print(f"Failed to delete entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to delete")


@router.get("/{id}")
async def get_by_id(id: str):
    try:
        result = await tarea_logic.get_by_id(id)
        return result
    except Exception as e:
        print(f"Failed to retrieve entry: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to retrieve")


# GET ALL
@router.get("/")
async def get_all(
    responsable: Optional[str] =  Query(None),
    descripcion: Optional[str] = Query(None)
):
    try:
        filter = {}
        if responsable:
            filter["responsable"] = {"$regex": ".*{}.*".format(responsable), "$options": "i"}
        if descripcion:
            filter["descripcion"] = {"$regex": ".*{}.*".format(descripcion), "$options": "i"}

        usuarios = await tarea_logic.get(filter)
        return usuarios

    except Exception  as e:
        print(f"Upload failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Retrieve failed")
