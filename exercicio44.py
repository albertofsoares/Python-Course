#####################################
#
# EXERCICIO 44
#
# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#
# à vista dinheiro ou cheque: 10% de desconto
#
# à vista no cartão: 5% de desconto
#
# em até 2x no cartão: preço normal
#
# 3x ou mais no cartão: 20% de juros

desc_din = 0.10
desc_card = 0.05
parc_3x = 0.20

valor = float(input('Digite o valor do produto: R$'))
print('Como você deseja pagar pelo produto?')
print('[0] Dinheiro ou Cheque')
print('[1] À Vista no Cartão')
print('[2] Parcelado em 2 vezes')
print('[3] Parcelado em 3 vezes ou mais')
escolha = int(input('Digite a opção desejada: '))

if escolha == 0:
    per_desc = valor * desc_din
    valor_final = valor - (valor * desc_din)
    print(f'O produto custando R${valor:.2f} com pagamento\n\
no dinheiro ou cheque fica por R${valor_final:.2f}')
elif escolha == 1:
    per_desc = valor * desc_card
    valor_final = valor - (valor * desc_card)
    print(f'O produto custando R${valor:.2f} com pagamento\n\
à vista no cartão fica por R${valor_final:.2f}')
elif escolha == 2:
    parcelas = valor / 2
    print(f'O produto custando R${valor:.2f} com pagamento\n\
parcelado no cartão fica por 2x de R${parcelas:.2f} sem juros!')
elif escolha == 3:
    per_acres = valor * parc_3x
    valor_final = valor + (valor * parc_3x)
    print(f'O produto custando R${valor:.2f} com pagamento\n\
parcelado no cartão em 3x ou mais fica por R${valor_final:.2f} com 20% de acréscimo.')
else:
    print('Não reconheço essa opção.')