#####################################
#
# EXERCICIO 40
#
# Crie um programa que leia duas notas de um aluno
# e calcule sua média, mostrando uma mensagem no final,
# de acordo com a média atingida:
#
# Média abaixo de 5.0: Reprovado
#
# Média entre 5.0 e 6.9: Recuperação
#
# Média 7.0 ou supeior: Aprovado

nota = float(input('Digite a primeira nota do aluno: '))
nota1 = float(input('Digite a segunda nota do aluno: '))

media = nota + nota1 / 2

if media >= 7.0:
    print(f'A média do(a) aluno(a) é de {media}, parabéns.')
    print('Este(a) seu(ua) aluno(a) está aprovado(a)')
elif media >= 5.0 and media <= 6.9:
    print(f'A média do(a) aluno(a) é de {media}, tem chance!')
    print('Este(a) seu(ua) aluno(a) está em recuperação.')
else:
    print(f'A média do(a) aluno(a) é de {media}, que pena.')
    print('Este(a) seu(ua) aluno(a) está reprovado(a).')