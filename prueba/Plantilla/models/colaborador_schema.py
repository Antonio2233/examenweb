from pydantic import BaseModel, Field, HttpUrl, field_validator
from datetime import datetime, timezone, timedelta
from typing import List
from typing import Literal


class Habilidad(BaseModel):
    nombre: str = Field(...,description="nombre de habilidades")
    # estado: Literal["aceptada", "pendiente"] = Field("pendiente", title="Estado de la invitación")

class colaboradorSchema(BaseModel):
    email: str = Field(...)
    nombre: str = Field(...)
    habilidades : List[Habilidad] = Field(default_factory=list,description="Lista de habilidades")
