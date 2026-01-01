#####################################
#
# EXERCICIO 45
#
# Crie um programa que faça o computador
# jogar jokenpô com você.

import random
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']

opcao = random.choice(opcoes)

escolha = input('Escolha entre pedra, papel e tesoura: ').lower()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('Escolha do computador: ', opcao)
print(f'Sua escolha: {escolha}')

# PEDRA X PAPEL
if opcao == 'pedra' and escolha == 'papel':
    print('Você ganhou')
# PAPEL X PEDRA
elif opcao == 'papel' and escolha == 'pedra':
    print('Você perdeu!')
# TESOURA X PEDRA
elif opcao == 'tesoura' and escolha == 'pedra':
    print('Você ganhou!')
# PEDRA X TESOURA
elif opcao == 'pedra' and escolha == 'tesoura':
    print('Você perdeu!')
# PAPEL X TESOURA
elif opcao == 'papel' and escolha == 'tesoura':
    print('Você ganhou!')
# TESOURA X PAPEL
elif opcao == 'tesoura' and escolha == 'papel':
    print('Você perdeu!')
# EMPATES
elif opcao == escolha:
    print('Empate!')
else:
    print("Não conheço essa opção!")