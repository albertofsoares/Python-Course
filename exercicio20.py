#####################################
#
# EXERCICIO 20
#
# O mesmo professsor do desafio anterior
# quer sorterar a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatros
# alunos e mostre a ordem sorteada.
#

import random 

nome = input('Digite o nome do Aluno 1: ')
nome1 = input('Digite o nome do Aluno 2: ')
nome2 = input('Digite o nome do Aluno 3: ')
nome3 = input('Digite o nome do Aluno 4: ')

ordem = [nome, nome1, nome2, nome3]

random.shuffle(ordem)

print(f'A ordem de apresentação escolhida foi:\n{ordem}')
