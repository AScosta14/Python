# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 046 ======')
# Faça um programa que mostra na tela uma contagem
# regressiva para estourar fogos de artifício, indo
# de 10 até 0 , com uma pausa de 1 segundo entre eles.

import time

for i in range(10,-1,-1):
    print(i)
    time.sleep(1)

print('Fogos de Artificio!!!')
    
