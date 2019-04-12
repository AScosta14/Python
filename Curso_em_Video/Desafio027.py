# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 027 ======')
# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro  o último nome separadamente.

name = str(input('Insira seu nome completo: ')).strip()

print('Primeiro Nome: {} \nÚltimo Nome: {}'.format(name.split()[0], name.split()[len(name.split()) - 1]))