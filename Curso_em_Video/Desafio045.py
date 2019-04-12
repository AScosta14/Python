# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 045 ======')
# Crie um programa que faça o computador jogar JOKEMPÔ com você.

import random as rd

run = 0

while run == 0:

    print('')
    print('====== JOKEMPÔ ========')
    print('')
    
    # Rodada do Jogador
    print('1 - Pedra')
    print('2 - Papel')
    print('3 - Tesoura')
    op = int(input('Selecione uma das 3 opções: '))

    if (op < 1 or op > 3):
        print('Opção Inválida! Tente novamente')
        print('')
        print('1 - Pedra')
        print('2 - Papel')
        print('3 - Tesoura')
        op = int(input('Selecione uma das 3 opções: '))

    if (op == 1):
        gamer = 'Pedra'
    elif (op == 2):
        gamer = 'Papel'
    else:
        gamer = 'Tesoura'

    # Rodada do Computador
    computer = rd.choice(['Pedra', 'Papel', 'Tesoura'])

    if (gamer == computer):
        print('')
        print('Jogador escolheu: {:s}'.format(gamer))
        print('Computador escolheu: {:s}'.format(computer))
        print('')
        run = 0
    else:
        print('')
        print('Jogador escolheu: {:s}'.format(gamer))
        print('Computador escolheu: {:s}'.format(computer))
        print('')
        if (gamer == 'Pedra' and computer == 'Tesoura'):
            print('Pedra ganha de Tesoura. Jogador venceu!')
        elif (gamer == 'Pedra' and computer == 'Papel'):
            print('Pedra perde do Papel. Computador venceu!')
        elif (gamer == 'Papel' and computer == 'Pedra'):
            print('Papel ganha da Pedra. Jogador venceu!')
        elif (gamer == 'Papel' and computer == 'Tesoura'):
            print('Papel perde da Tesoura. Computador venceu!')
        elif (gamer == 'Tesoura' and computer == 'Papel'):
            print('Tesoura vence do Papel. Jogador venceu!')
        elif (gamer == 'Tesoura' and computer == 'Pedra'):
            print('Tesoura perde da Pedra. Computador venceu!')

        print('')
        run = int(input('Deseja jogar novamente? 0 - Sim ou 1 - Não '))

        if (run != 0 and run != 1):
            print('Opção Inválida! Tente novamente')
            run = int(input('Deseja jogar novamente? 1 - Sim ou 2 - Não '))
