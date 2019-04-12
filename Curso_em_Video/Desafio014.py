# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 014 ======')
# Escreva um programa que converta temperaturas

Escala = input('Informe qual escala de temperatura (C - Celcius/ F - Fahrenheit/ K - Kelvin): ')

if Escala == "C" or Escala == "c":
	C = float(input('Temperatura em Celcius: '))
	K = C + 273.
	F = 1.8*C + 32.
	print('Temperatura em Fahrenheit: {:.2f}ºF \nTemperatura em Kelvin: {:.2f}K'.format(F, K))
elif Escala == "K" or Escala == "k":
	K = float(input('Temperatura em Kelvin: '))
	C = K - 273.
	F = 1.8*(K - 273.) + 32.
	print('Temperatura em Celcius: {:.2f}ºC \nTemperatura em Fahrenheit: {:.2f}ºF'.format(C, F))
elif Escala == "F" or Escala == "f":
	F = float(input('Temperatura em Fahrenheit: '))
	C = (F - 32.)/1.8
	K = (F - 32.)/1.8 + 273.
	print('Temperatura em Celcius: {:.2f}ºC \nTemperatura em Kelvin: {:.2f}K'.format(C, K))
else:
	print('Escala Termométrica INEXISTENTE!!!')

