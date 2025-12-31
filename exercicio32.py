#####################################
#
# EXERCICIO 32
#
# Faça um programa que leia um ano qualquer
# e mostre se ele é bissexo.

ano = int(input('Digite o ano deseja verificar: '))

div_por4 = ano % 4
div_por100 = ano % 100
div_por400 = ano % 400

bissexto = div_por4 + div_por100 + div_por400

if bissexto == 0:
    print('Este ano é bissexto!')
else:
    print('Este ano não é bissexto.')

    
# As regras podem ser resumidas assim:
# Divisível por 4? Se sim, siga para a próxima regra. Se não, não é bissexto.
# Divisível por 100? Se sim, siga para a próxima regra. Se não, é bissexto.
# Divisível por 400? Se sim, é bissexto. Se não, não é bissexto. 