#####################################
#
# EXERCICIO 52
#
# Faça um programa que leia um número inteiro
# e diga se ele é ou não um número primo

# primo = divisivel por 1 e por ele mesmo e apenas.


num = int(input('Digite um número: '))
divs = 0
for c in range(1, num+1, 1):
    if num % c == 0:
        divs += 1
if divs == 2:
    print('Numero Primo!')
print('fim')