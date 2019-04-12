# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 009 ======')
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Insira um número inteiro qualquer: '))
print('Tabuada do {}'.format(num))
for i in range(0,11):
	print('{} X {}  = {}'.format(num, i, num*i))
