# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 044 ======')
# Elabore um programa que calcule o valor a ser pago por um produto
# considerando seu preço normal e a condição de pagamento

preco = float(input('Preço do Produto: R$ '))

print('')
print('1 - À vista (dinheiro)')
print('2 - À vista (cartão)')
print('3 - 2x no Cartão')
print('4 - 3x ou mais no Cartão')
print('')
forma_pgt = int(input('Selecione a forma de pagamento: '))

if (forma_pgt == 1):
    print('Preço do produto é: R$ {:.2f}'.format(0.9*preco))
elif (forma_pgt == 2):
    print('Preço do produto é: R$ {:.2f}'.format(0.95*preco))
elif (forma_pgt == 3):
    print('Preço do produto é: R$ {:.2f}'.format(1*preco))
elif (forma_pgt == 4):
    print('Preço do produto é: R$ {:.2f}'.format(1.2*preco))
else:
    print('Forma de Pagamento Inválida')

