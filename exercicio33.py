#####################################
#
# EXERCICIO 33
#
# Faça um programa que leia três números
# e mostre qual é o maior e qual é o menor

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

menor = num1
maior = num1

if num2 < menor:
    menor = num2

if num3 < menor:
    menor = num3

if num2 > maior:
    maior = num2

if num3 > maior:
    maior = num3

print(f'O maior número é: {maior}')
print(f'O menor número é: {menor}')