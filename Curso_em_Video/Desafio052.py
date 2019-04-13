# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 052 ======')
# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

num = int(input('Insira um número inteiro: '))

if(num == 1):
    print('O número 1 é primo por falta de divisores!')
else:
    for i in range(2,num):
        if (num%i == 0):
            print('O número {:d} não é primo!'.format(num))
            print('Seu primeiro divisor é {:d}'.format(i))
            break
    if(i == (num-1)):
        print('O número {:d} é primo!'.format(num))
