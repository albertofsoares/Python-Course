################################################
#
# EXERCICIO 05
#
# Crie um programa que leia quanto dinheiro uma pessoa tem
# na carteira e mostre quantos Dólares ela pode comprar.
#
dinheiro = float(input('Quanto de dinheiro você tem? R$'))
print('Você pode comprar ${} dólares para viajar!'.format(dinheiro//3.27))