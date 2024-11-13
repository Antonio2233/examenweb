from database import MONGOCRUD
from models.evento_schema import Invitados
from bson import ObjectId  # Importar ObjectId desde bson
import item_logic.usuario as usuariologic
from typing import Optional, List
from datetime import datetime, timedelta

class EventoCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Evento')

    async def add_invitado(self, id: str, email: str):
            try:

                evento = await self.get_id(id)

                if evento:

                    lista = await usuariologic.get_contactos(evento['anfitrion'])

                    if email in lista:
                        nuevo_invitado = Invitados(useremail=email, estado="pendiente")

                        await self.collection.update_one(
                            {"_id": ObjectId(id)},  # Buscar el evento por su _id
                            {"$addToSet": {"invitados": nuevo_invitado.model_dump()}}  # Inserta no duplicados
                        )

                        return {"message": "Invitado añadido."}

            except Exception as e:
                print(f"Error al obtener el evento: {str(e)}")
                return None

    async def aceptar(self, id: str, email: str):
                try:

                    updatedItem = False
                    evento = await self.get_id(id)
                    if evento:
                        print(evento['anfitrion'])
                        anfitrionEntidad = await usuariologic.get_user(evento['anfitrion'])
                        print(anfitrionEntidad)
                        if anfitrionEntidad and email in anfitrionEntidad['contactos']:
                            updatedItem = await self.collection.update_one(
                                {"_id": ObjectId(id), "invitados.useremail": email},
                                {
                                    "$set": {"invitados.$.estado": "aceptada"}
                                }
                            )

                    return bool(updatedItem)

                except Exception as e:
                    print(f"Error al obtener el evento: {str(e)}")
                    return None

    async def reprogramar(self,id: str, year: Optional[int] = None, month: Optional[int] = None, day: Optional[int] = None):
        try:
                # Buscar el evento original
                evento = await self.get_id(id)
                if not evento:
                    return {"message": "Evento no encontrado."}

                # Obtener la fecha de inicio del evento original
                fecha_inicio = evento['inicio']
                if isinstance(fecha_inicio, str):
                    fecha_inicio = datetime.fromisoformat(fecha_inicio.replace("Z", "+00:00"))  # Convertir a datetime UTC

                nueva_fecha = fecha_inicio

                # Sumar años manualmente
                if year:
                    nuevo_anio = nueva_fecha.year + year
                    nueva_fecha = nueva_fecha.replace(year=nuevo_anio)

                # Sumar meses manualmente
                if month:
                    nuevo_mes = nueva_fecha.month + month
                    nuevo_anio = nueva_fecha.year

                    # Ajustar el año si se pasa de diciembre
                    while nuevo_mes > 12:
                        nuevo_mes -= 12
                        nuevo_anio += 1

                    nueva_fecha = nueva_fecha.replace(year=nuevo_anio, month=nuevo_mes)

                # Sumar días usando timedelta
                if day:
                    nueva_fecha += timedelta(days=day)

                # Crear el nuevo evento con la nueva fecha de inicio
                nuevo_evento = evento.copy()
                nuevo_evento['inicio'] = nueva_fecha.isoformat() + "Z"  # Convertir de nuevo al formato ISO con 'Z'
                nuevo_evento['_id'] = ObjectId()  # Generar un nuevo ID para el nuevo evento

                # Insertar el nuevo evento en la base de datos
                await self.create_item(nuevo_evento)

                return {"message": "Evento reprogramado exitosamente."}

        except Exception as e:
            print(f"Error al reprogramar el evento: {str(e)}")
            return {"message": "Error al reprogramar el evento."}