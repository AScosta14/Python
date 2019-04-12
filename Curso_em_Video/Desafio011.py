# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 011 ======')
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a
# quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2.

largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))

area = largura*altura
tinta = area/2

print('Voce precisará de {:.3f} litros de tinta para pintar a parede!'.format(tinta))
