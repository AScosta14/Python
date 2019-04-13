# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 054 ======')
# Crie um programa que leia o ano de nascimento de
# sete pessoas. No final, mostre quantas pessoas ainda
# não atingiram a maioridade e quantas já são maiores.

from datetime import date

# Ano Atual
ano_atual = date.today().year

maior = 0
menor = 0


for i in range(1,8):
    # Ano de Nascimento
    ano_nasc = int(input('Ano de Nascimento da {:d} pessoa: '.format(i)))
    if(ano_atual - ano_nasc >= 18):
        maior = maior + 1
    else:
        menor = menor + 1

print('Numero de Pessoas que atingiram a maioridade: {:d}'.format(maior))
print('Numero de Pessoas que não atingiram a maioridade: {:d}'.format(menor))
