# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

from datetime import date

print('====== DESAFIO 041 ======')
# A confederação de natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre
# a sua categoria de acordo com a idade.

# Data Atual
data_atual = date.today().year

# Ano de Nascimento
nasc = int(input('Qual o seu ano de nascimento? '))

idade = data_atual - nasc

if (idade < 9):
    print('Sua categoria é: MIRIM')
elif (9 <= idade and idade < 14):
    print('Sua categoria é: INFANTIL')
elif (14 <= idade and idade < 19):
    print('Sua categoria é: JUNIOR')
elif (idade == 19 or idade == 20):
    print('Sua categoria é: SÊNIOR')
else:
    print('Sua categoria é: MASTER')


    
        
    
    
