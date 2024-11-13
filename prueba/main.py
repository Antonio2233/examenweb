from fastapi import FastAPI
from routes import usuario_route,evento_route

app = FastAPI()

app.include_router(usuario_route.router, prefix="/usuarios")
app.include_router(evento_route.router, prefix="/eventos")