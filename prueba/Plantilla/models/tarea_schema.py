from pydantic import BaseModel, Field, HttpUrl, field_validator
from typing import List



class tareaSchema(BaseModel):
    responsable: str = Field(...,description="Dirección de email del usuario responsable de la tarea (el que crea la tarea).")
    descripcion: str = Field(..., max_length=50,description="Descripción breve de la tarea (hasta 50 caracteres)..")
    segmentos: int = Field(...,description="Duracion estimada")
    habilidades : List[str] = Field(default_factory=list,description="Lista de habilidades")

    # model_config = {
    #     "json_schema_extra" : {
    #         "example": {
    #             "email": "usuario@ejemplo.com",
    #             "nombre": "Juan Pérez",
    #             "contactos": ["contacto1@ejemplo.com", "contacto2@ejemplo.com"]
    #             }
    #         }
    # }