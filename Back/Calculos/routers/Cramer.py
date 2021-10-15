from fastapi import APIRouter, status, HTTPException
from Calculos.repository import Cramer
from Calculos import schemas
import numpy as np

router = APIRouter(
	prefix="/Cramer",
	tags=['Cramer']
)

@router.post('/SemDP', status_code=status.HTTP_200_OK)
def CramerSemDP(request: schemas.Sistema):
	return {"Response": Cramer.CramerSemDP(np.array(request.matriz))} 

@router.post('/ComDP', status_code=status.HTTP_200_OK)
def CramerDP(request: schemas.Sistema):
    return {"Response": Cramer.CramerDP(np.array(request.matriz))} 
