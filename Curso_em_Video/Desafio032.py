# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 032 ======')
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

from datetime import date

year = int(input('Insira um ano qualquer OU digite 0 para o ano atual: '))

if year == 0:
	year = date.today().year #Ano atual da máquina.
	
if year < 1582:
	print('Ano Inválido!!!')
else:
	if year % 400 == 0:
		print('Ano de {} é Bissexto.'.format(year))
	else:
		if year % 4 == 0 and year % 100 != 0:
			print('Ano de {} é Bissexto.'.format(year))
		else:
			print('Ano de {} não é Bissexto.'.format(year))

