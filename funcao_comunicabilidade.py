# -*- coding: utf-8 -*-
'''
Importações e Instalações necessárias
'''
import numpy as np
from math import *


def matriz_comunicabilidade(matriz, n):
  '''
  Funcao que calcula a Comunicabilidade
  :parametro matriz: matriz de adjacencia 
  :parametro n: numero de termos da serie a ser considerado  
  '''

  matriz_padrao = matriz.copy()
  matriz_suporte_1 = matriz.copy()
  matriz_c = np.identity(len(matriz), float)
  matriz_c += matriz_padrao

  for k in range(2,n+1):
    
    if k > 1:
      
      # Eleva a matriz por k vezes
      matriz_padrao = np.matmul(matriz_padrao, matriz_suporte_1)
      matriz_suporte_2 = matriz_padrao/factorial(k)


      # soma as n matrizes
      matriz_c += matriz_suporte_2
  
  return matriz_c