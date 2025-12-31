################################################
#
# EXERCICIO 06
#
# Crie um programa que leia a largura e a altura de uma parede em metros
# calcule a sua área e a quantidade de tinta necessária  para pinta-la
# sabendo que cada litro de tinta pinta uma área de 2m²
#
#
a = float(input('Quanto tem de altura? '))
l = float(input('Quanto tem de largura? '))
area = a * l
quantidade = area / 2
#
print('Para pintar uma área de {} metros você precisa de {} litros de tinta'.format(area, quantidade))
#
# poderia ser assim também (utilizando f-string's)
#
# alt = float(input('Altura da parede (m): '))
# larg = float(input('Largura da parede (m): '))
#
# area = alt * larg
# tinta = area / 2
#
# Usando f-string e limitando a 2 casas decimais com :.2f
# print(f'Sua parede tem a dimensão de {alt}x{larg} e sua área é de {area:.2f}m².')
# print(f'Para pintar essa parede, você precisará de {tinta:.2f}l de tinta.')
