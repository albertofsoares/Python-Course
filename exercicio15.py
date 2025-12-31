# Escreva um programa que pergunte a quantidade de Km percorridos 
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#  Calcule o preço a pagar, 
# sabendo que o carro custa R$60 por dia 
# e R$0,15 por Km rodado

# Escreva um programa que calcule os dias e os km percorridos de um carro
# alugado, levando em consideração que o carro custa R$60 por dia e também
# custa R$0,15 por KM rodado

diaria = 60
custo_km = 0.15

kilometragem = int(input('Digite a kilometragem percorrida: '))
dias_alugado = int(input('Quantos dias o veiculo ficou alugado? '))

aluguel = dias_alugado * diaria
custo = custo_km * kilometragem
total = aluguel + custo

print(f'O aluguel do veículo ficou no total de R${aluguel:.2f} \
      \nmais a kilometragem que ficou em R${custo:.2f}, \
      \ntotalizando R${total:.2f}')