# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 30 ======')
# Crie um programa que leia um número inteiro e mostre se ele é par ou ímpar.

num = int(input('Insira o número: '))

if num % 2 == 0:
	print('O número {} é PAR!'.format(num))
else:
	print('O número {} é ÍMPAR!'.format(num))
	
