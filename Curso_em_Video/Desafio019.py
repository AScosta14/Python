# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 019 ======')
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo
# o nome deles e escrevendo o nome do escolhido.

import random as rd
import numpy as np

alunos = []
for i in range(0,4):
	name = input('Nome do(a) Aluno(a): ')
	alunos.append(name)

print(alunos)
sort = rd.choice(alunos)
print('O aluno sorteado foi {}'.format(sort))
