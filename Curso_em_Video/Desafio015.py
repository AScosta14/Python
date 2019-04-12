# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 015 ======')
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Quantos Quilometros você percorreu com o carro? '))
dias = int(input('Durante quantos dias? '))

preco = 60.*dias + 0.15*km

print('O preço do aluguel do carro foi de R$ {:.2f}'.format(preco))