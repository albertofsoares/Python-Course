#####################################
#
# EXERCICIO 50
#
# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares
# se o valor digitado for impar, desconsidere.

soma = 0 
for c in range(0, 6):
    num = int(input('Digite um número: '))
    par = num % 2
    if par == 0:
        soma = soma + num
    else:
        print('Número impar, desconsiderado')
print(f'O resultado é de: {soma}')
    