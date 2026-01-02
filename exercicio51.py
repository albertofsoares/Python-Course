#####################################
#
# EXERCICIO 51
#
# Desenvolva um programa que leia o primeiro termo
# e a razão de uma Progressão Aritmética.
#
# No final, mostre os 10 primeiros termos dessa progressão.

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao

for c in range (termo, decimo + razao, razao):
    print(c)
print(f'Estes são os 10 primeiros termos dessa progressão.')