# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 008 ======')
# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milimetros
# (e também nas outras escalas de comprimento)

m = float(input('Insira uma medida em metros: '))
print('Em Quilometro(km): {} \nEm Hectometro(hm): {} \nEm Decâmetro(dam): {}'.format(m/1000, m/100, m/10))
print('Em Decímetro(dm): {} \nEm Centímetro(cm): {} \nEm Milímetro(mmm): {}'.format(m*10, m*100, m*1000))
