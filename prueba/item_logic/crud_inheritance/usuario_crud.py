from database import MONGOCRUD
from models.usuario_schema import usuarioSchema
from typing import List
from bson import ObjectId  # Importar ObjectId desde bson


class UsuarioCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Usuario')

    async def get_contactos(self, email: str) -> List[str]:
        try:
            usuario = await self.collection.find_one({"email": email})

            return usuario['contactos']
        except Exception as e:
            print(f"Error al obtener los contactos: {str(e)}")
            return []

    async def get_user(self, email: str):
        try:
            usuario = await self.collection.find_one({"email": email})

            if usuario:
                usuario["_id"] = str(usuario["_id"])  # Convertir ObjectId a string
            return usuario
        except Exception as e:
            print(f"Error al obtener el usuario: {str(e)}")
            return None

    async def add_contact(self, email: str,contacto: str):
        try:
            usuario = await self.collection.find_one({"email": email})

            if usuario:
                await self.collection.update_one(
                        {"email": email},
                        {"$push": {"contactos": contacto}}  # Añadir el contacto a la lista
                    )

                return {"message": "Contacto añadido."}
            else:
                return {"message": "Usuario no encontrado."}

        except Exception as e:
            print(f"Error al obtener el usuario: {str(e)}")
            return None


    async def delete_contact(self, email: str, contacto: str):
        try:
            if not contacto:
                return False
            usuario = await self.collection.find_one({"email": contacto})
            item = await self.collection.find_one({"email": email})

            if item and usuario:
                updatedItem = await self.collection.update_one(
                    {"email": email},
                    {
                    "$pull": {"contactos": contacto}
                    }
                )
                return bool(updatedItem)

            else:
                return {"message": "Usuario no encontrado."}

        except Exception as e:
            print(f"Error al eliminar el contacto: {str(e)}")
            return {"message": "Error al eliminar el contacto."}



    async def get_contactos_dupla(self, email: str, nombrecontacto : str) -> List[str]:
        try:
            usuario = await self.collection.find_one({"email": email})

            if usuario:

                lista = usuario['contactos']
                result = []

                for item in lista:
                    cont = await self.collection.find_one({"email": item})
                    base = cont['nombre']
                    print(base)
                    if nombrecontacto in base:
                        dupla = [cont['email'],cont['nombre']]
                        result.extend(dupla)

                return result
        except Exception as e:
            print(f"Error al obtener los contactos: {str(e)}")
            return []