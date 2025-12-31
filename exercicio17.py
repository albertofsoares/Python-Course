#####################################
#
# EXERCICIO 17
#
# Crie um programa que leia o comprimento do cateto oposto
# e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa
#

cateto_oposto = float(input('Digite o cateto oposto: '))
cateto_adjacente = float(input('Digite o cateto adjacente: '))

import math

quadrado_oposto = math.pow(cateto_oposto, 2)
quadrado_adjacente = math.pow(cateto_adjacente, 2)
soma_catetos = quadrado_oposto + quadrado_adjacente
raiz = math.sqrt(soma_catetos)

print(f'O comprimento da Hipotenusa é {raiz}')

# PODERIA SER RESOLVIDO DA SEGUINTE FORMA (via: Gemini IA)
#
# import math

# cateto_oposto = float(input('Digite o cateto oposto: '))
# cateto_adjacente = float(input('Digite o cateto adjacente: '))

# # A função hypot faz os quadrados, a soma e a raiz tudo de uma vez
# hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)

# print(f'O comprimento da Hipotenusa é {hipotenusa:.2f}')