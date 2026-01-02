#####################################
#
# EXERCICIO 56
#
# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 PESSOAS
# no final do programa mostre:
#
# a média de idade do grupo
# qual o nome do homem mais velho
# quantas mulheres tem menos de 20 anos

maior = 0
menor = 0
menores = 0
soma_idade = 0

for c in range(1, 2+1, 1):
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o genero da pessoa: ')).lower()
    soma_idade += idade
    if c == 1:
        idade > maior
        maior = idade
        menor = idade
        if sexo == 'feminino' and idade < 20:
            menores += 1
    else:
        if idade < menor:
            menor = idade

        if idade > maior:
            maior = idade
media = soma_idade / 4
print(f'A maior idade é: {maior} e a menor é {menor}')
print(f'Existe {menores} mulheres menores de 20.')
print(f'A media de idade é de {media}')


#######################################################

#####################################
# EXERCICIO 56
# Analisador Completo

soma_idade = 0
maior_idade_homem = 0
nome_homem_velho = ''
total_mulheres_20 = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    # 1. Acumulando a idade para a média
    soma_idade += idade
    
    # 2. Lógica do Homem mais velho
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_homem_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem_velho = nome
        
    # 3. Lógica das Mulheres com menos de 20 anos
    if sexo == 'F' and idade < 20:
        total_mulheres_20 += 1

# Calculando a média fora do laço
media = soma_idade / 4

print('\n' + '='*30)
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_velho}.')
print(f'Ao todo são {total_mulheres_20} mulheres com menos de 20 anos.')

    