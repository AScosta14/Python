# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 036 ======')
# Escreva um programa para aprovar o empréstimo bancário para a compra de
# uma casa. O programa vai perguntar o valor da casa, o salário do comprador
# e em quantos anos ele vai pagar. Calcule o valor da prestação mensal sabendo
# que não pode exceder 30% do salário ou o empréstimo será negado.

home_value = float(input('Preço da Casa: '))
salario = float(input('Salário do Comprador: '))
tempo = int(input('Quantos anos deseja pagar: '))

mensalidade = home_value/(12*tempo)

if (mensalidade >= 1.3*salario):
    print('Seu salário é: R$ {:.2f}'.format(salario))
    print('Prestação Mensal da Casa: R$ {:.2f}'.format(mensalidade))
    print('Empréstimo NEGADO!')
else:
    print('Seu salário é: R$ {:.2f}'.format(salario))
    print('Prestação Mensal da Casa: R$ {:.2f}'.format(mensalidade))
    print('Empréstimo APROVADO!')

