# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 026 ======')
# Faça um programa que leia uma frase pelo teclado e mostre:
# >>> Quantas vezes aparece a letra A
# >>> Em que posição ela aparece pela primeira vez
# >>> Em que posição ela aparece pela última vez

phrase = str(input('Insira uma frase qualquer: ')).strip()

if phrase.upper().find('A') == -1:
	print('Sua frase não tem letra A!!!!')
else:
	print('A letra A aparece {} vezes na frase. \nEla aparece pela primeira vez na posição {} e pela última vez na posição {}'.format(phrase.upper().count('A'),
		 phrase.upper().find('A') + 1, phrase.upper().rfind('A') + 1))

