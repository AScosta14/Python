# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 031 ======')
# Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem,
# cobrando R$ 0,50 por km para viagens de até 200 km e R$ 0,45 ara viagens mais longas.

km = float(input('Insira a distância da viagem em quilômetros: '))

if km <= 200.:
	print('Preço da Viagem é R$ {:.2f}'.format(km * 0.50))
else:
	print('Preço da Viagem é R$ {:.2f}'.format(km * 0.45))

