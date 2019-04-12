# coding=utf-8
# CURSO EM VÍDEO
# Curso de Programação em Python
# Professor: Gustavo Guanabara

print('====== DESAFIO 021 ======')
# Faça um programa em Python que abre e reproduz o áudio de arquivo MP3.

import pygame

pygame.init()
pygame.mixer.music.load('Rick_and_Morty.mp3')
pygame.mixer.music.play()
pygame.event.wait()
