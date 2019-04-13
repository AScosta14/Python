# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 049 ======')
# Refaça o Desafio009.py, mostrando a tabuada de um número
# que o usuário escolher, só utilizando o laço for.

num = int(input('Insira um número: '))

print('Tabuada de {:d}'.format(num))
for i in range(1,11):
    print('{:d} X {:d} = {:d}'.format(num, i, num*i))


