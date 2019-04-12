# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 018 ======')
# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

ang = float(input('Insira um ângulo em graus: '))
rad = math.radians(ang)
print("Ângulo em Radianos: {}".format(rad))
print('Seno de {}º vale {:.2f} \nCosseno de {}º vale {:.2f} \nTangente de {}º vale {:.2f}'.format(ang, math.sin(rad), ang, math.cos(rad), ang, math.tan(ang)))