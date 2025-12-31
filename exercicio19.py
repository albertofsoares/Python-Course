#####################################
#
# EXERCICIO 19
#
# Um professor quer sortear um dos seus quatro alunos
# para apagar o quadro. Faça um programa que ajude ele,
# lendo o nome deles e escrevendo o nome escolhido.
#

import random

nome = input('Digite o nome do aluno 1: ')
nome1 = input('Digite o nome do aluno 2: ')
nome2 = input('Digite o nome do aluno 3: ')
nome3 = input('Digite o nome do aluno 4: ')

ordem = [nome, nome1, nome2, nome3]
sorteio = random.choice(ordem)
import random

print(f'O aluno sorteado foi {sorteio}')