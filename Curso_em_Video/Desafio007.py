# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 007 ======')
# Desenvolva um programa que leia duas notas de um aluno, calcule e mostre a sua média.

nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2

print('Média do Aluno é {:.2f}'.format(media))

if media >= 7.0 and media < 10.0:
	print('Aluno APROVADO')
elif media >= 4.0 and media < 7.0:
	print('Aluno de AF')
else:
	print('Aluno REPROVADO')
