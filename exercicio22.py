#####################################
#
# EXERCICIO 22
#
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# 
# O nome com todas as letras maiúsculas
#
# O nome com todas as letras minúsculas
#
# Quantas letras ao todo (sem contar espaços)
#
# quantas letras tem o primeiro nome
#
nome = input('Digite o seu nome: ')

maisculo = nome.upper()
minusculo = nome.lower()
tamanho = len(nome)
espaco = nome.count(' ') 
total = tamanho - espaco

lista = nome.split()
primeiro = lista[0]
letras_primeiro = len(primeiro)

print(f'{nome} em maiúsculo fica: {maisculo}\n\
e {nome} em minúsculo fica: {minusculo}\n\
O tamanho de {nome} é {total} caracteres\n\
o primeiro nome tem {letras_primeiro} caraceres')

# poderia ser assim: 
# primeiro = nome.find(' ')
# onde o find encontrar o primeiro espaço
# será exatamente o número de caracteres do
# primeiro nome pedido, ai só chamar a string.