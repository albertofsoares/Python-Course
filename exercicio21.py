#####################################
#
# EXERCICIO 21
#
# Faça um programa em Python que abra e reproduza 
# o audio de um arquivo MP3
#

import pygame

print('Carregando som... [50%]')
pygame.init()

print('Carregando som... [100%]')
pygame.mixer.music.load('audio.mp3')

print('Audio tocando...')
pygame.mixer.music.play()

# Isso mantém o programa aberto até você dar ENTER no terminal
input('Ouvindo a música? Aperte Enter para parar...')