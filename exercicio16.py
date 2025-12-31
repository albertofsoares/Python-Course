#####################################
#
# EXERCICIO 16
#
# Crie um programa que leia um número real qualquer
# pelo teclado e mostre na tela sua porção inteira
#
# exemplo: Digite um número: 6.127
# o número 6.127 tem a parte inteira 6.
#

numero = float(input('Digite um número decimal: '))

from math import trunc

n_int = trunc(numero)
print(f'A parte inteira de {numero} é: {n_int}')

# poderia ser resolvido sem importar biblioteca nenhuma, 
# da seguinte forma:
# numero = float(input('Digite um número decimal: '))
# print(f'A parte inteira de {numero} é: {int(numero)}')
