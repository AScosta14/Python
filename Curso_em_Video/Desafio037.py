# Escreva um programa que leia um número inteiro
# qualquer e peça para o usuário escolher qual será
# a base de conversão.

num = int(input('Digite um número inteiro: '))

print('''Escolha uma base para a conversão:
[1] - Base Binária
[2] - Base Octal
[3] - Base Hexadecimal''')

option = int(input('Sua opção: '))

while (option < 1 or option > 3):
    option = int(input('Opção Inválida! Tente novamente: '))

if (option == 1):
    print('O número {} na base binária é {}.'.format(num, bin(num)[2:]))
elif (option == 2):
    print('O número {} na base octal é {}.'.format(num, oct(num)[2:]))
else:
    print('O número {} na base hexadecimal é {}.'.format(num, hex(num)[2:]))
