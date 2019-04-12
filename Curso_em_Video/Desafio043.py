# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 043 ======')
# Desenvolva uma lógica que leia o peso e a altura de uma pessoa
# e calcule o seu IMC (Índice de Massa Corpórea)

# peso
weight = float(input('Qual o seu peso? '))
# altura
height = float(input('Qual a sua altura? '))

IMC = weight/(height**2)

if (IMC < 18.5):
    print('Seu IMC é {:.2f}, você está abaixo do peso!'.format(IMC))
elif (IMC >= 18.5 and IMC < 25):
    print('Seu IMC é {:.2f}, você está com o peso normal!'.format(IMC))
elif (IMC >= 25 and IMC < 30):
    print('Seu IMC é {:.2f}, você está com sobrepeso!'.format(IMC))
else:
    print('Seu IMC é {:.2f}, você está com obesidade mórbida!'.format(IMC))
