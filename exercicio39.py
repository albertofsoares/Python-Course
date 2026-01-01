#####################################
#
# EXERCICIO 39
#
# Crie um programa que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade:
#
# Se ele ainda vai se alistar ao serviço militar.
#
# Se é a hora de se alistar.
#
# Se já passou do tempo do alistamento.
#
# Seu programa também deverá mostrar o tempo que falta
# ou o tempo que passou do prazo.

idade = int(input('Qual é a sua idade? '))

alistamento = 17
alist_obgt = 18

if idade <= 17:
    tempo = alist_obgt - idade 
    print('Você ainda não precisa se alistar.')
    print(f'Falta {tempo} anos para você se alistar!')
elif idade == 18:
    print('Chegou a hora de se alistar!')
    print('pois você completou 18 anos.')
else:
    atraso = idade - alist_obgt
    print(f'Você está {atraso} anos atrasado!')
    print('Você deveria ter se alistado com 18 anos.')