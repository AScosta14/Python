# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 005 ======')
# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e o seu antecessor.

num = int(input('Digite um número inteiro: '))
ant_num = num - 1
suc_num = num + 1
print('O antecessor de {} é {} \nO sucessor de {} é {}'.format(num, ant_num, num, suc_num))
