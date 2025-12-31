#####################################
#
# EXERCICIO 35
#
# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo

reta = float(input('Digite o comprimento da reta: '))
reta1 = float(input('Digite o comprimento da segunda reta: '))
reta2 = float(input('Digite o comprimento da última reta: '))

soma1 = reta + reta1

if soma1 > reta2:
    soma2 = reta + reta2
    if soma2 > reta1:
        soma3 = reta1 + reta2
        if soma3 > reta:
            print('Podem formar um triângulo')
        else:
            print('Não podem formar um triangulo')
    else:
        print('Não podem formar um triangulo')
else:
    print('Não podem formar um triangulo')


# a = reta    b = reta1   c = reta2 

# regra de ouro:
# a + b > c
# a + c > b
# b + c > a