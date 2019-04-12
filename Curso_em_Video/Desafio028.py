# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 028 ======')
# Escreva um programa que faça o computador pensar em um número entre 0 e 5 e peça
# para o usuário tentar descobrir qual foi o número escolhido pelo computador
# O programa deverá escrever na tela se o usuário vencer ou perder.

import random as rd
from time import sleep

computador = rd.randint(0, 5) # Sorteio de um número aleatório.

jogador = int(input('Tente descobrir qual número o computador está pensando: '))
print('PROCESSANDO...')
sleep(3)
if computador == jogador:
	print('Parabéns, você VENCEU!!!')
else:
	print('Você PERDEU!!! O número sorteado foi {}'.format(computador))

