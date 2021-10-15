from fastapi import FastAPI
from Calculos.routers import Laplace, Cramer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=[""],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)

app.include_router(Laplace.router)
app.include_router(Cramer.router)

@app.get("/TesteAPI")
def Teste():
    return {"message": "Hello World"}