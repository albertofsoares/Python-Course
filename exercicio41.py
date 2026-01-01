#####################################
#
# EXERCICIO 41
#
# A confedereção Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre a sua
# categoria de acordo com a idade:
#
# Até 9 anos: MIRIM
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 20 anos: Sênior
# Acima: Master

nascimento = int(input('Digite seu ano de nascimento: '))
ano_atual = 2025
idade = ano_atual - nascimento 

if idade > 0 and idade <= 9:
    print(f'O aluno possui {idade} anos!')
    print('O aluno pertence a categoria Mirim')
elif idade > 9 and idade <= 14:
    print(f'O aluno possui {idade} anos!')
    print('O aluno pertence a categoria Infantil')
elif idade > 14 and idade < 19:
    print(f'O aluno possui {idade} anos!')
    print('O aluno pertence a categoria Junior')
elif idade >= 19 and idade <= 20:
    print(f'O aluno possui {idade} anos!')
    print('O aluno pertence a categoria Sênior')
else:
    print(f'O aluno possui {idade} anos!')
    print('O aluno pertence a categoria Master!')