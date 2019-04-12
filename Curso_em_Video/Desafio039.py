# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

from datetime import date

print('====== DESAFIO 039 ======')
# Faça um programa que leia o ano de nascimento
# de um jovem e informe a sua condição de alistamento militar

# Data Atual
data_atual = date.today().year

# Ano de Nascimento
nasc = int(input('Qual o seu ano de nascimento? '))

idade = data_atual - nasc

if (idade < 18):
    print('Você ainda não tem idade para se alistar, faltam {:d} anos!'.format(18-idade))
elif (idade == 18):
    print('Você está na idade de se alistar no serviço militar!')
else:
    print('Já passou {:d} anos do seu alistamento no serviço militar!'.format(idade-18))

