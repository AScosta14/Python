# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 010 ======')
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode
# comprar. (Use US$ 1,00 = R$ 3,27)

reais  = float(input('Quanto dinheiro você tem na carteira? R$ '))
print('Com esse dinheiro você pode comprar US$ {:.2f}'.format(reais/3.27))
