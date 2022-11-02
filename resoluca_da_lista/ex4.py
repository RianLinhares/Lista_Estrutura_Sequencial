# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('-'*30)
print('CÁLCULO DA MÉDIA'.center(30))
print('-'*30)
print('Digite as notas do aluno')
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segundo Nota: '))
n3 = float(input('Terceira Nota: '))
n4 = float(input('Quarta Nota: '))
media = (n1 + n2 + n3 + n4) / 4
print(f'A média do aluno é igual a {media:.2f}')