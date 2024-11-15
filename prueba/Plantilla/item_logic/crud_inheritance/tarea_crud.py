from database import MONGOCRUD
from models.tarea_schema import tareaSchema
from typing import List
from bson import ObjectId  # Importar ObjectId desde bson


class TareaCrud(MONGOCRUD):

    def __init__(self):
        super().__init__('Tarea')