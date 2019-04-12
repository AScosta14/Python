# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 032 ======')
# Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
num3 = int(input('Insira o terceiro número: '))

if num1 > num2 and num1 > num3:
	maior = num1
	if num2 > num3:
		menor = num3
	else:
		menor = num2
	print('O maior número é {} e o menor é {}'.format(maior, menor))
elif num2 > num1 and num2 > num3:
	maior = num2
	if num1 > num3:
		menor = num3
	else:
		menor = num1
	print('O maior número é {} e o menor é {}'.format(maior, menor))
elif num3 > num1 and num3 > num2:
	maior = num3
	if num1 > num2:
		menor = num2
	else:
		menor = num1
	print('O maior número é {} e o menor é {}'.format(maior, menor))
else:
	print('Devem existir números iguais!!')

