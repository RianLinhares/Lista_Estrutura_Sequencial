#Faça um Programa que calcule a área de um quadrado, em seguida mostre o
# dobro desta área para o usuário.

print('-'*60)
print(f'CÁLCULO DA ÁREA DE QUADRADO E SEU DOBLO')
print('-'*60)
l = float(input('Digite o lado do quadrado, em cm: '))
print('A área de um quadrado é dado por L²')
area = l**2
print(f'Área do quadrado = {area}')
print(f'Dobro da área = {area*2}')
