# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
from math import pi

print('-'*30)
print('CÁLCULO DA ÁREA DE UM CÍRCULO')
print('-'*30)
raio = float(input('Digite o raio do círculo, em cm: '))
print('A área de um círculo é dado por pi*r², logo com isso tem-se que')
print(f'Um círculo com raio de {raio} cm, tem uma aŕea, apresentada abaixo.')
area = pi*(raio**2)
print(f'área do círculo = {area:.2f}')
