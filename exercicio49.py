#####################################
#
# EXERCICIO 49
#
# Refaça o exercicio 09 mostrando a tabuado de um número
# que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um número: '))
cont = 1
x = n * cont

for c in range(1, 11, 1):
    print(f'{n} x {cont} = {x}')
    cont += 1
    x += n