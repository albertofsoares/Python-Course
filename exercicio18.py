#####################################
#
# EXERCICIO 18
#
# Crie um programa que leia um ângulo qualquer
# e mostre na tela o valor do seno, cosseno 
# e o tangente desse ângulo
#

angulo = float(input('Digite um ângulo: '))

import math

radianos = math.radians(angulo)
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f'O seno de {angulo} é {seno:.5f},\n\
o cosseno de {angulo} é {cosseno:.5f}\n\
o tangente de {angulo} é {tangente:.5f}')

# .math.sin(x): Seno de x
# .math.cos(x): Cosseno de x
# .math.tan(x): Tangente de x
# .math.radians(x): Converte o ângulo de graus para radianos.