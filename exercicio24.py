#####################################
#
# EXERCICIO 24
#
# Crie um programa que leia o nome de uma cidade e diga
# se ela começa ou não com o nome "SANTO".
#

cidade = input('Qual o nome da sua cidade? ')
minuscula = cidade.lower()
espacos = cidade.strip()
print('Essa cidade começa com "Santo"? ', minuscula[:5] == 'santo')
