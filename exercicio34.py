#####################################
#
# EXERCICIO 34
#
# Crie um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento salarial

# para salários superiores a R$ 1.250,00
# calcule um aumento de 10%

# Para os salários inferiores a R$ 1.250,00
# calcule um aumento de 15%

salario = float(input('Digite o seu salário atual: '))

aumento10 = 0.10
aumento15 = 0.15

if salario >= 1250:
    reajuste = salario * aumento10
    novo_salario = salario + reajuste
    print(f'Seu salário de {salario:.2f} passará para {novo_salario:.2f}')
    print(f'Totalizando R${reajuste:.2f} de aumento salarial.')
else:
    reajuste = salario * aumento15 
    novo_salario = salario + reajuste 
    print(f'Seu salário de {salario:.2f} passará para {novo_salario:.2f}')
    print(f'Totalizando R${reajuste:.2f} de aumento salarial.')
    
# multiplica o Salário Antigo pela % (em decimal) 
# e somar ao valor original para achar o novo salário,
