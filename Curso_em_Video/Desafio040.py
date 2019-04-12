# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 040 ======')
# Crie um programa que leia duas notas de um aluno e calcule
# a sua média e a sua situação.

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))

media = 0.5*(nota1 + nota2)

if (media < 5.0):
    print('Média Final é {:.2f}'.format(media))
    print('Situação do Aluno: REPROVADO')
elif (media >= 5.0 and media < 7.0):
    print('Média Final é {:.2f}'.format(media))
    print('Situação do Aluno: RECUPERAÇÃO')
else:
    print('Média Final é {:.2f}'.format(media))
    print('Situação do Aluno: APROVADO')


    
