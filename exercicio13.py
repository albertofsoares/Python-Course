################################################
#
# EXERCICIO 08
#
# Crie um programa que leia o salário de um funcionário e mostre
# seu novo salário com 15% de aumento.
#
salario = float(input('Digite o seu salário: R$'))
aumento = (15 / 100) * salario
total = aumento + salario
print(f'O aumento de 15% em cima de {salario:.2f} fica um total de {aumento:.2f}, totalizando R${total:.2f}')