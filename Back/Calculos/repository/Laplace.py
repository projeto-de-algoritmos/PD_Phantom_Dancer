from fastapi import HTTPException, status
import numpy as np
import math

memo = {}

def LaplaceSemDP(Matriz):
  
  if(Matriz.shape == (1,1)):
    return Matriz[0][0] 
  
  soma = 0
  alternador = 1
  for i in range(len(Matriz)):
    subMatriz = np.delete(Matriz, (0), axis=0)
    subMatriz = np.delete(subMatriz, (i), axis=1)
    soma += LaplaceSemDP(subMatriz) * Matriz[0][i] * alternador
    alternador*=-1
  return soma

def LaplaceDP(Matriz):
  if(len(Matriz) == (1)):
    return Matriz[0][0] 

  if Matriz in memo:
    print("NHA")
    return memo[Matriz]
  
  soma = 0
  alternador = 1
  for i in range(len(Matriz)):
    subMatriz = np.delete(Matriz, (0), axis=0)
    subMatriz = np.delete(subMatriz, (i), axis=1)

    aux = []

    for t in range(len(subMatriz)):
      aux_intern = []
      for k in range(len(subMatriz[t])):
        aux_intern.append(subMatriz[t][k])
      aux.append(tuple(aux_intern))

    subMatriz = tuple(aux)
  

    soma += LaplaceDP(subMatriz) * Matriz[0][i] * alternador
    alternador*=-1
  
  memo[Matriz] = soma

  return soma