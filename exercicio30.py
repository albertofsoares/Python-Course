#####################################
#
# EXERCICIO 30
#
# Crie um programa que leia um número inteiro qualquer
# e mostre na tela se ele é par ou impar.

numero = int(input('Digite um número: '))

resto = (numero % 2)

if resto == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')

#if % de n1 / 2 = 0