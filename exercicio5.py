

################################################
#
# EXERCICIO 05
#
# Faça um programa que leia algo pelo telcado e mostre na tela.
# o seu tipo primitivo e todas as informações possíveis sobre ela.

texto = input('Digite algo: ')

print('O tipo primitivo é: ', type(texto))
print('É númerico? ', texto.isnumeric())
print('É texto? ', texto.isalpha())
print('É alpha numerico? ', texto.isalnum())
print('É minusculo?: ', texto.islower())
print('É maisculo? ', texto.isupper())
print('É um espaço? ', texto.isspace())
print('Está capitalizada? ', texto.istitle())
