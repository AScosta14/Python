# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 025 ======')
# Crie um programa que leia o nome de uma pessoa e diga se ela tem 'Silva' no nome.

name = str(input('Insira seu nome completo: ')).strip()
# 'silva' in name.lower()   True or False?

if name.upper().find('SILVA') == -1:
	print('Seu nome não tem Silva!')
else:
	print('Seu nome tem Silva!')

