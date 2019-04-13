# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 051 ======')
# Desenvolva um programa que leia o primeiro termo e
# a razão de uma P.A. e no final mostre os 10 primeiros
# termos dessa progressão

a1 = float(input('Insira o primeiro termo da P.A. : '))
r = float(input('Insira a razão da P.A. : '))

an = a1
print('Progressão Aritmética (P.A.)')
for i in range(1,11):
    print(an)
    an = an + r
