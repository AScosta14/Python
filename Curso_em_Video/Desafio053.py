# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 053 ======')
# Crie um programa que leia uma frase qualquer e diga
# se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Insira uma frase qualquer: '))
frase = frase.replace(' ','')
contrario = frase[::-1]

for i in range(0,len(frase)):
    if (frase[i] != contrario[i]):
        print('A frase não é um Palíndromo!')
        break

if (i == len(frase)-1):
    print('A frase é um Palíndromo!')
