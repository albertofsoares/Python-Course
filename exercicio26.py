#####################################
#
# EXERCICIO 26
#
# Crie um programa que leia uma frase pelo teclado e mostre:
#
# Quantas vezes aparece a letra "A".
#
# Em que posição ela aparece a primeira vez
#
# Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
minusculo = frase.lower()
cont = frase.count('a')
print('A letra "a" aparece', cont, 'vezes')
primeira = minusculo.find('a')
print('Nº do Caractere do primeiro "a":', primeira)
ultima = minusculo.rfind('a')
print('Nº do Caractere do último "a":', ultima)