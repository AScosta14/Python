# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 012 ======')
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Insira o preço do produto: R$ '))
print('O preço original é R$ {:.2f}, mas com o desconto de 5% custará R$ {:.2f}'.format(preco, preco - preco*0.05))
