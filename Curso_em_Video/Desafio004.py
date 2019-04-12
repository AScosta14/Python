# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 004 ======')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu
# tipo primitivo e todas as informações possíveis spbre ele.

ent = input('Digite algo pelo teclado: ')

print('O tipo primitivo do que voce digitou é {}'.format(type(ent))) # Tipo primitivo
print('A entrada fornecida tem apenas espaços?: {}'.format(ent.isspace())) # Apenas espações
print('A entrada fornecida é numérica?: {}'.format(ent.isnumeric())) # Numérica
print('A entrada fornecida é alfabética?: {}'.format(ent.isalpha())) # Alfabética
print('A entrada fornecida é alfa-numérica?: {}'.format(ent.isalnum())) # Alfa-numérica
print('A entrada está em MAIÚSCULO?: {}'.format(ent.isupper())) # Letras MAIÚSCULAS
print('A entrada está em MINÚSCULO?: {}'.format(ent.islower())) # Letras minúsculas
print('A entrada está capitalizada?: {}'.format(ent.istitle())) # Capitalização