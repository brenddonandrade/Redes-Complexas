
'''
Bibliotecas usadas
'''

import numpy as np
class Grafo:
    '''
    Classe grafo    
    '''

    def __init__(self, vertices):
        ''' Construtor do objeto grafo
        :parametro vertcies:  numero de nos do grafo
        '''

        self.vertices = vertices
        self.grafo = np.zeros((vertices, vertices), int)


    def adiciona_aresta(self, u, v):
        '''
        Adiciona uma aresta nao direcionada
        :param u: vertice a ser incrementado aresta com v
        :param v: =     =   =   =   =   =   =   =   =   u
        '''

        self.grafo[u-1][v-1] = 1
        self.grafo[u-1][v-1] = 1


    def mostra_matriz(self):
        '''
        Retorna uma matriz para que possa ser salva num arquivo txt
        '''

        matriz = []
        for i in range(self.vertices):
            matriz.append(self.grafo[i])
        return matriz



    def calc_grau(self):
        '''
        Calcula o grau do vertice retornando uma coluna com os graus de cada vertice
        '''

        grau = []
        for i in range(self.vertices):
            grau.append(sum(self.grafo[i]))
        return grau


grafo1 = Grafo(3)

grafo1.adiciona_aresta(2,3)
grafo1.adiciona_aresta(1,3)

matriz = grafo1.mostra_matriz()

np.savetxt('matriz.txt', matriz, fmt='%d')


grau = grafo1.calc_grau()

np.savetxt('grau.txt', grau, fmt='%d')