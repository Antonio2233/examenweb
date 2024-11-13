from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import List


class usuarioSchema(BaseModel):
    email: str = Field(...)
    nombre: str = Field(...)
    contactos : List[str] = Field(default_factory=list,description="Lista de contactos")

    model_config = {
        "json_schema_extra" : {
            "example": {
                "email": "usuario@ejemplo.com",
                "nombre": "Juan Pérez",
                "contactos": ["contacto1@ejemplo.com", "contacto2@ejemplo.com"]
                }
            }
    }