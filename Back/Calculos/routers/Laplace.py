from fastapi import APIRouter, status, HTTPException
from Calculos.repository import Laplace 
from Calculos import schemas
import numpy as np

router = APIRouter(
	prefix="/Laplace",
	tags=['Laplace']
)

@router.post('/SemDP', status_code=status.HTTP_200_OK)
def LaplaceSemDP(request: schemas.Matriz):
	return { "Response": Laplace.LaplaceSemDP(np.array(request.matriz))} # LaplaceDP().karatsuba(request)

@router.post('/ComDP', status_code=status.HTTP_200_OK)
def LaplaceDP(request: schemas.Matriz):
    Laplace.memo = {}
    return { "Response": Laplace.LaplaceDP(Parser(request.matriz)) } # LaplaceDP().karatsuba(request)

def Parser(matriz):
  aux = []
  for t in range(len(matriz)):
      aux_intern = []
      for k in range(len(matriz[t])):
        aux_intern.append(matriz[t][k])
      aux.append(tuple(aux_intern))
  return tuple(aux)
