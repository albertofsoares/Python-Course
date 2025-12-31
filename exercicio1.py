################################################
#
# EXERCICIO 01
#
# Crie um script Python que leia o nome da pessoa
# e mostre uma mensagem de boas vindas de acordo
# com o valor digitado
#
nome = input('Qual o seu nome?')
print('Olá', nome, 'prazer em conhecer você!')

# poderia ser também:

nome = input('Qual o seu nome? ')
print('É um prazeer te conhecer, {}'.format(nome))