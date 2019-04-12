# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 042 ======')
# Refaça o Desafio035.py dos triângulos
# acrescentando o recurso de mostrar que tipo
# de triângulo será formado.

a = float(input('Medida da primeira reta: '))
b = float(input('Medida da segunda reta: '))
c = float(input('Medida da terceira reta: '))

import numpy as np

if np.abs(b-c) < a < b+c and np.abs(a-c) < b < a+c and np.abs(a-b) < c < a+b:
        print('Com estas retas é possível formar um triângulo ', end='')
        if a == b == c:
                print('EQUILÁTERO!')
        elif a != b != c != a:
                print('ESCALENO!')
        else:
                print('ISÓSCELES!')
else:
        print('Com estas retas não é possível formar um triângulo.')

