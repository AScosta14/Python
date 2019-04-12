# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 029 ======')
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80 km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por cada
# km acima do limite.

speed = float(input('Qual a velocidade registrada? '))

if speed <= 80:
	print('Motorista prudente! Continue dirigindo assim!')
else:
	print('INFRAÇÃO!!! Limite de Velocidade ultrapassado, compareça ao DETRAN e pague uma multa no valor de R$ {:.2f}'.format((speed - 80)*7))

