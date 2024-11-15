from fastapi import FastAPI
from routes import colaborador_route, tarea_route

app = FastAPI()

app.include_router(tarea_route.router, prefix="/tareas")
app.include_router(colaborador_route.router, prefix="/colaboradores")