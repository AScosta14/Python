# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 023 ======')
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

# Apesar de existir o modo matemático, vamos usar os recursos das strings
num = input('Insira um número de 0 a 9999: ')

if len(num) == 1:
	print('Unidades: {}'.format(num[0]))
elif len(num) == 2:
	print('Unidades: {} \nDezenas: {}'.format(num[1], num[0]))
elif len(num) == 3:
	print('Unidades: {} \nDezenas: {} \nCentenas: {}'.format(num[2], num[1], num[0]))
elif len(num) == 4:
	print('Unidades: {} \nDezenas: {} \nCentenas: {} \nMilhares: {}'.format(num[3], num[2], num[1], num[0]))
else:
	print('Número fora dos padrões exigidos!!!')

