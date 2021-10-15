from pydantic import BaseModel
from typing import List

class Matriz(BaseModel):
	matriz: List[List[float]] = [[1,2,3],[4,5,6],[7,8,15]]

class Sistema(BaseModel):
	matriz: List[List[float]] = [[1,1,-3,0],[1,-2,1,3],[2,-3,2,8]]