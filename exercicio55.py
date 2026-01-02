#####################################
#
# EXERCICIO 55
#
# Faça um programa que leia o peso de cinco pessoas,
# no final mostre qual foi o maior e o menor peso lidos.

# menor = 0
# maior = 0

# for c in range(0, 5+1, 1):
#     peso = float(input('Digite o peso: '))
#     if peso >= maior:
#         maior = peso
#     else:
#         menor = peso
# print(f'O maior peso é {maior} kg e o menor peso é {menor} kg')

# maior = 0
# menor = 0

# for c in range(0, 2+1, 1):
#     peso = float(input('Digite o peso: '))

# if c == 0:
#     maior = peso
#     menor = peso
# else:
#     if peso <= maior:
#         menor = peso 
    
#     if peso >= menor:
#         maior = peso
# print(f'O maior peso é {maior} kg e o menor peso é {menor} kg')

########################################

menor = 0
maior = 0

for c in range(1, 5+1, 1):
    peso = float(input('Digite o peso: '))
    if c == 1:
        menor = peso 
        maior = peso
    else:
        if peso > maior:
            maior = peso

        if peso < menor:
            menor = peso
print(f'O maior peso foi de {maior}')
print(f'E o menor peso foi de {menor}')