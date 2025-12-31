################################################
#
# EXERCICIO 07
#
# Crie um programa que leia um preço de um produto e mostre
# seu novo preço, agora com 5% de desconto
#
preco = float(input('Digite o valor do produto: R$'))
desconto = (preco * 5 / 100)
n_preco = preco - desconto
#
print(f'O valor do produto de R${preco:.2f} ficou por R${n_preco:.2f} tendo um total de R${desconto:.2f} de desconto.')
