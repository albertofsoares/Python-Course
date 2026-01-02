#####################################
#
# EXERCICIO 54
#
# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final mostre quantoas pessoas ainda não atingiram
# a maioridade e quantas já são maiores de idade.

maioridade = 21
ca = 0
cm = 0
for c in range(0, 7, 1):
    ano = int(input('Qual o ano de nascimento?'))
    ano_atual = 2025
    idade = ano_atual - ano
    if idade < maioridade:
        cm += 1
    else:
        ca += 1
print(f'Existem {cm} menores e {ca} maiores de idade')