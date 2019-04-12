# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 022 ======')
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# >>> O nome com todas as letras maiúsculas
# >>> O nome com todas as letras minúsculas
# >>> Quantas letras ao todo(sem considerar espaços)
# >>> Quantas letras tem o primeiro nome.

name = input('Insira seu nome completo: ')

letras = len(name) - name.count(' ')

print('Nome maiúsculo: {} \nNome minúsculo: {} \nNúmero de letras do nome completo: {} \nNúmero de letras do primeiro nome: {}'.format(name.upper(), 
	name.lower(), letras, len(name.split()[0])))