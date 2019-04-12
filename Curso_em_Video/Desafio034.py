# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 034 ======')
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$ 1250,00 calcule um aumento de 10%. Para salários inferiores um aumento de 15%.

salario = float(input('Insira o salário do funcionário: R$ '))

if salario >= 1250.:
	print('Novo salário com aumento de 10% é R$ {:.2f}'.format(salario + salario*0.10))
else:
	print('Novo salário com aumento de 15% é R$ {:.2f}'.format(salario + salario*0.15))

