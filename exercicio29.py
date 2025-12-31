#####################################
#
# EXERCICIO 29
#
# Escreva um programa que leia a velocidade de um carro.
#
# Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo
# que ele foi multado por excesso de velocidade.
#
# A multa vai custar R$ 7.00 por cada KM acima do limite

km_perm = 80.00
multa = 7.00

velocidade = float(input('Digite a velocidade atual do veículo: '))

if velocidade > km_perm:
    print('Você foi multado por excesso de velocidade')
    excesso = velocidade - km_perm 
    valor_multa = multa * excesso
    print(f'O valor da multa é de {valor_multa}')
else:
    print('Você está dentro do limite de velocidade')