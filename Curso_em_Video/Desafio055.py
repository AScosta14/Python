# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 055 ======')
# Faça um programa que leia o peso de cinco pessoas.
# No final mostre qual foi o maior e o menor peso lidos.

peso = float(input('Peso da 1 pessoa: '))
maior = peso
menor = peso
for i in range(2,6):
    peso = float(input('Peso da {:d} pessoa: '.format(i)))
    if (peso > maior):
        maior = peso
    elif (peso < menor):
        menor = peso

print('Maior Peso Inserido: {:.1f} Kg'.format(maior))
print('Menor Peso Inserido: {:.1f} Kg'.format(menor))
