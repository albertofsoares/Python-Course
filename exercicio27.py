#####################################
#
# EXERCICIO 27
#
# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente
# Ex: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite seu nome completo: ')

lista = nome.split()

print('Seu nome profissional é:', lista[0], lista[-1])