'''Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta
é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas
de tinta a serem compradas e o preço total.'''

area = float(input('Área a ser pintada: '))
litro = 3*area
quantidade = litro / 18
valor = quantidade * 80
print(f'Quantidade de latas: {quantidade} latas')
print(f'Valor a ser pago: {valor} R$')
