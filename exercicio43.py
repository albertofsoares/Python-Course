#####################################
#
# EXERCICIO 43
#
# Desenvolva uma lógica que leia o peso e a altura de uma pesssoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#
# Abaixo de 18.5: Abaixo do Peso
#
# Entre 18.5 e 25: Peso ideal
#
# 25 até 30: sobrepeso
#
# 30 até 40: Obesidade
#
# Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite o seu peso atual: '))

imc = peso / (altura * altura)

if imc < 18.5:
    print('Você está abaixo do Peso!')
elif imc >= 18.5 and imc < 25:
    print('Você está no seu Peso Ideal')
elif imc >= 25 and imc < 30:
    print('Você está com Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Você está com Obesidade')
elif imc > 40:
    print('Você está com Obesidade Morbida.')
else:
    print('IMC Desconhecido!!!')