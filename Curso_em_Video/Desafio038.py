# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 038 ======')
# Escreva um programa que leia dois números inteiros e compare-os.

num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))

if (num1 > num2):
    print('{:d} é maior que {:d}!'.format(num1,num2))
elif (num1 < num2):
    print('{:d} é maior que {:d}!'.format(num2,num1))
else:
    print('{:d} e {:d} são iguais!'.format(num1,num2))

