# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 048 ======')
# Faça um programa que calcule a soma de todos os números ímpares
# que são múltiplos de 3 e que se encontram de 1 até 500.

soma = 0
for i in range(1,501):
    if (i%2 == 1 and i%3 == 0):
        print(i)
        soma = soma + i

print('Soma dos Impares Multiplos de 3 é: {:d}'.format(soma))
