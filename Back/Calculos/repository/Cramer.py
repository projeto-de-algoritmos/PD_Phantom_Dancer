from fastapi import HTTPException, status
from . import Laplace
import numpy as np


def CramerSemDP(Sistema):
  vIndependentes = Sistema[0:,-1]
  Sistema = np.delete(Sistema, (-1), axis=1)

  Respostas = []

  D = Laplace.LaplaceSemDP(Sistema)

  if D == 0:
    return "Sem solução ou infinitas soluções"
  
  for i in range(len(Sistema)):
    subSistema = Sistema.copy()
    subSistema[:,i] = vIndependentes
    Respostas.append(Laplace.LaplaceSemDP(subSistema)/D)
  return Respostas

def CramerDP(Sistema):
  vIndependentes = Sistema[0:,-1]
  Sistema = np.delete(Sistema, (-1), axis=1)

  Respostas = []

  D = Laplace.LaplaceDP(Parser(Sistema))

  if D == 0:
    return "Sem solução ou infinitas soluções"
  
  for i in range(len(Sistema)):
    subSistema = Sistema.copy()
    subSistema[:,i] = vIndependentes
    Respostas.append(Laplace.LaplaceDP(Parser(subSistema))/D)
  return Respostas

def Parser(matriz):
  aux = []
  for t in range(len(matriz)):
      aux_intern = []
      for k in range(len(matriz[t])):
        aux_intern.append(matriz[t][k])
      aux.append(tuple(aux_intern))
  return tuple(aux)