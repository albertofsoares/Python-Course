#####################################
#
# EXERCICIO 37
#
# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão
#
# 1 - para binário              # bin(num)
# 2 - para octal                # oct(num)
# 3 - para hexadecimal          # hex(num)

num = int(input('Digite um número: '))

print('--------------------------------------')
print('[1] para exibir o valor binário')
print('[2] para exibir o valor octal')
print('[3] para exibir o valor hexadecimal')
escolha = int(input('Digite a opção desejada: '))

if escolha == 1:
    binario = bin(num)
    print(f'O valor binário de {num} é {binario}')
elif escolha == 2:
    octal = oct(num)
    print(f'O valor octal de {num} é {octal}')
elif escolha == 3:
    hexadecimal = hex(num)
    print(f'O valor hexadecimal de {num} é {hexadecimal}')
else:
    print(f'A opção {escolha} não está no menu.')

