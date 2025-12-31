#####################################
#
# EXERCICIO 25
#
# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.

nome = input('Digite seu nome: ')

silva = 'silva' in nome.lower().strip()
print('Seu nome tem Silva?', silva)