#####################################
#
# EXERCICIO 42
#
# Refaça o exercicio 35 dos triângulos,
# acrescentando o recurso de mostrar que tipo
# de triângulo será formado:
#
# Equilátero: Todos os lados iguais
#
# Isósceles: Dois lados iguais
#
# Escaleno: Todos os lados diferentes


reta = float(input('Digite o comprimento da reta: '))
reta1 = float(input('Digite o comprimento da segunda reta: '))
reta2 = float(input('Digite o comprimento da última reta: '))

soma1 = reta + reta1
soma2 = reta + reta2
soma3 = reta1 + reta2

if soma1 > reta2 and soma2 > reta1 and soma3 > reta:
    print('Podem formar um triângulo')
    if reta == reta1 == reta2:
        print('Triângulo do tipo Equilátero.')
    elif reta != reta1 and reta1 != reta2 and reta != reta2:
        print('Triângulo do tipo Escaleno')
    else:
        print('Triângulo do tipo Isósceles')
else:
    print('Não podem formar um triangulo')


# a = reta    b = reta1   c = reta2 

# regra de ouro:
# a + b > c
# a + c > b
# b + c > a