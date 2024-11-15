from database import MONGOCRUD
from models.colaborador_schema import Habilidad
from bson import ObjectId  # Importar ObjectId desde bson
import item_logic.tarea as tarealogic
from typing import Optional, List
from datetime import datetime, timedelta



class ColaboradorCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Colaborador')

    async def delete_secundario_by(self,email: str):
        deleted = False
        item = await self.collection.find_one({'email': email})
        if item:
            await self.collection.delete_one({"email": email})
            deleted = True
        return deleted

    async def update_secundario_by(self,email: str, data: dict):
        if not data:
            return False
        item = await self.collection.find_one({'email': email})
        # item = await self.collection.find_one({"email": ObjectId(email)})

        if item:
            updatedItem = await self.collection.update_one(
                {"email": email}, {"$set": data}
            )
            return bool(updatedItem)

        return False


    async def get_habilidades_crud(self, email: str) -> List[str]:
        try:
            colaborador = await self.collection.find_one({"email": email})

            return colaborador['habilidades']
        except Exception as e:
            print(f"Error al obtener los habilidades: {str(e)}")
            return []

    async def add_habilidad(self, email: str,nombre: str):
        try:
            usuario = await self.collection.find_one({"email": email})
            new_contacto = Habilidad(nombre=nombre)
            if usuario:
                await self.collection.update_one(
                        {"email": email},
                        {"$push": {"habilidades": new_contacto.model_dump()}}  # Añadir el contacto a la lista
                    )

                return {"message": "Habilidad añadida."}
            else:
                return {"message": "Colaborador no encontrado."}

        except Exception as e:
            print(f"Error al obtener el usuario: {str(e)}")
            return None


    async def delete_habilidad_crud(self, email: str,nombre: str):
        try:
            if not email:
                return False
            usuario = await self.collection.find_one({"email": email})


            if usuario:
                updatedItem = await self.collection.update_one(
                    {"email": email},
                    {
                    "$pull": {"habilidades": {"nombre": nombre}}
                    }
                )
                return bool(updatedItem)

            else:
                return {"message": "Usuario no encontrado."}

        except Exception as e:
            print(f"Error al eliminar el contacto: {str(e)}")
            return {"message": "Error al eliminar el contacto."}
