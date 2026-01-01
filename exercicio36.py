#####################################
#
# EXERCICIO 36
#
# Escreva um programa para aprovar o empréstimo  bancário
# para a compra de uma casa.
#
# O programa vai perguntar o valor da casa, o salário do comprador,
# e em quantos anos ele vai pagar.
#
# Calcule o valor da prestação mensal, sabendo que ela não pode
# exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual o valor do imóvel? R$'))
salario = float(input('Quanto você recebe por mês? R$'))
prazo = int(input('Em quantos anos você irá pagar? '))
parcela_max = (salario * 30) / 100

parcelas = prazo * 12
mensalidade = valor_casa / parcelas

if mensalidade > parcela_max:
    print('Não foi possível aprovar o seu empréstimo.')
else:
    print(f"Parabéns, o imóvel custando R${valor_casa:.2f} pode ser financiado!")
    print(f'Você irá pagar {parcelas} prestações de R${mensalidade:.2f} por mês')