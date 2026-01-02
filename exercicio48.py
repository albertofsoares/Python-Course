#####################################
#
# EXERCICIO 48
#
# Faça um programa que calcule a soma entre os números ímpares
# que são múltimos de três e que se encontram no intervalo de 1 até 500

i = 1
f = 500
s = 0
cont = 0

for c in range(i, f+1, 3):
    resto = c % 3
    if resto == 0:
        s += c
        cont += 1
print(f'Foram somados {cont} números e o resultado é: {s}')