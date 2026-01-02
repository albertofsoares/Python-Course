#####################################
#
# EXERCICIO 53
#
# Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços.
#
# Exemplo: Apos a Sopa

frase = str(input('Digite uma frase: ')).replace(' ', '')
tamanho = len(frase)
inverso = ''
for c in range(tamanho-1, -1, -1):
    inverso += frase[c]
    print(f'Testando: a letra da posição {c} é {frase[c]}')
print(f'A frase original: {frase}')
print(f'A frase invertida: {inverso}')

if frase == inverso:
    print('Temos um PALÍNDROMO!')
else:
    print('Não é um palíndromo.')

# Dicas de Ouro para começar:

# Limpeza: Você vai precisar tirar os espaços da frase 
# (use .strip() e .replace(' ', '')).

# Inversão: Você precisa criar uma versão da frase "ao contrário".

# O for invertido: Você pode usar um for que começa na última letra 
# e vai até a primeira, vindo para trás (range(fim, inicio, -1)).