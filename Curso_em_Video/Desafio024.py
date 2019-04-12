# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 024 ======')
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'Santo'.

city = str(input('Insira o nome da cidade: ')).strip()
# print(city[:5].upper() == 'SANTO')

if city.split()[0].upper() != 'SANTO':
	print('A cidade {} não começa com o nome Santo.'.format(city))
else:
	print('A cidade {} começa com o nome Santo.'.format(city))

