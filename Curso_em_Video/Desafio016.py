# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

import math

print('====== DESAFIO 016 ======')
# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

num = float(input('Insira um número real: '))
inteira = math.trunc(num)
quebrada = num - inteira
print('A parte inteira de {} é {} e a parte quebrada é {:.3f}'.format(num, inteira, quebrada))
