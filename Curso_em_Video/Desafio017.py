# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

from math import sqrt, pow

print('====== DESAFIO 017 ======')
# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

cat_op = float(input('Valor do Cateto Oposto: '))
cat_ad = float(input('Valor do Cateto Adjacente: '))

hip = sqrt(pow(cat_op, 2) + pow(cat_ad, 2))
print('Valor da Hipotenusa: {:.3f}'.format(hip))
