# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 035 ======')
# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Medida da primeira reta: '))
b = float(input('Medida da segunda reta: '))
c = float(input('Medida da terceira reta: '))

import numpy as np

if np.abs(b-c) < a < b+c and np.abs(a-c) < b < a+c and np.abs(a-b) < c < a+b:
	print('Com estas retas é possível formar um triângulo.')
else:
	print('Com estas retas não é possível formar um triângulo.')

