#####################################
#
# EXERCICIO 23
#
# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos digitos separados
#
# Exemplo:
#
# Digite um número: 1834
#
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = int(input('Digite um número (0 a 9999): '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Milhar: {milhar}\n\
Centena: {centena}\n\
Dezena: {dezena}\n\
Unidade: {unidade}')

# numero = str(input('Digite um número de 0 a 9999: '))
# unidade = numero[0]
# dezena = numero[1]
# centena = numero[2]
# milhar = numero[3]

# print(unidade, dezena, centena, milhar)

# print(f'Milhar: {unidade}\n\
# Centena: {dezena}\n\
# Dezena: {centena}\n\
# Unidade: {milhar}')