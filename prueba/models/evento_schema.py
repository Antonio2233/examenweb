from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime, timezone, timedelta
from typing import List
from typing import Literal


class Invitados(BaseModel):
    useremail: str = Field(...)
    estado: Literal["aceptada", "pendiente"] = Field("pendiente", title="Estado de la invitación")

class eventoSchema(BaseModel):
    anfitrion: str = Field(...)
    descripción: str = Field(..., max_length=50,description="Descripcion.")
    inicio: datetime = Field(default_factory=lambda:datetime.now(timezone(timedelta(hours=2))), description="Fecha de la edición")
    duracion: int = Field(...,description="Duracion del evento en tramos de 15 minutos")
    invitados : List[Invitados] = Field(default_factory=list,description="Lista de invitados")


    @field_validator('duracion')
    def validar_duracion(cls, value):
        if value % 15 != 0:
            raise ValueError("La duración debe ser un múltiplo de 15 minutos")
        return value

    @field_validator('inicio')
    def validar_duracion(cls, value):
        if value.minute % 15 != 0:
            raise ValueError("El inicio debe ser un múltiplo de 15 minutos")
        return value