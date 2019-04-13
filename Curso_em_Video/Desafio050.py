# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 050 ======')
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.

soma = 0
for i in range(1,7):
    num = int(input('Insira o {:d} número inteiro: '.format(i)))
    if (num%2 == 0):
        soma = soma + num

print('A soma dos números pares é: {:d}'.format(soma))
