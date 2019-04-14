# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 056 ======')
# Desenvolva um programa que leia o nome, a idade e
# o sexo de 4 pessoas. No final mostre: 1. A média das
# idades; 2. Nome do homem mais velho; 3. Quantas
# mulheres tem menos de 20 anos.

nome = str(input('Nome do(a) Usuário(a): '))
idade = float(input('Idade do(a) Usuário(a): '))
sexo = str(input('Sexo do(a) Usuário(a): '))
print('')

media = idade
velho = ''
id_velho = 0
if (idade > id_velho and sexo == 'Masculino'):
    velho = nome
    id_velho = idade
velhas = 0

if (idade < 20 and sexo == 'Feminino'):
    velhas = velhas + 1

for i in range(2,5):
    nome = str(input('Nome do(a) Usuário(a): '))
    idade = float(input('Idade do(a) Usuário(a): '))
    sexo = str(input('Sexo do(a) Usuário(a): '))
    print('')
    
    media = media + idade

    if (idade > id_velho and sexo == 'Masculino'):
        velho = nome
        id_velho = idade

    if (idade < 20 and sexo == 'Feminino'):
        velhas = velhas + 1

print('A média das idades é {:.1f}'.format(media/4))

if(velho != ''):
    print('O homem mais velho é {:s}'.format(velho))
else:
    print('Não há homens nesta lista!')
print('Quantidade de Mulheres com menos de 20 anos: {:d}'.format(velhas))
