#####################################
#
# EXERCICIO 31
#
# Crie um programa que pergunte a distância de uma viagem em km
# Calcule o preço da passagem cobrando R$0,50 por km
# para viagens até 200 km 
# e cobrando R$0,45 para viagens mais longas

passagem = 0.50
promocional = 0.45

dist = float(input('Digite a distância em KM: '))

if dist <= 200:
    calculo = passagem * dist
    print(f'A passagem irá custar: R${calculo:.2f}')
else:
    calculo = promocional * dist
    print(f'A passagem irá custar: R${calculo:.2f}')

