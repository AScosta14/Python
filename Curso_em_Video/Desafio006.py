# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

import math

print('====== DESAFIO 006 ======')
# Crie um algoritmo que leia um número e mostre o dobro, o triplo e a raiz quadrada.

num = float(input('Insira um número: '))
dobro = num*2
triplo = num*3
rquad = math.sqrt(num) # ou rquad = num**(1/2)

print('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {}'.format(num, dobro,
 num, triplo, num, rquad))