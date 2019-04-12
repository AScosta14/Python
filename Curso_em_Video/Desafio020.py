# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 020 ======')
# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem de apresentação.

import random as rd
import numpy as np

alunos = []
for i in range(0,4):
	name = input('Nome do(a) Aluno(a): ')
	alunos.append(name)

sort = []
for i in range(0,4):
	sort.append(rd.choice(alunos))
	id = alunos.index(sort[i])
	del alunos[id]

print('A ordem de apresentação dos trabalhos é: \n1º {} \n2º {} \n3º {} \n4º {}'.format(sort[0], sort[1], sort[2], sort[3]))

# Obs! Existe o comando random.shuffle(list) que embaralha uma lista.