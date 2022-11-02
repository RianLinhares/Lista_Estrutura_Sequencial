#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#a) o produto do dobro do primeiro com metade do segundo .
#b) a soma do triplo do primeiro com o terceiro.
#c) o terceiro elevado ao cubo.

nint1 = int(input('Digite o primeiro número inteiro: '))
nint2 = int(input('Digite o segundo número inteiro: '))
nreal = float(input('Digite o número real: '))
a = (2 * nint1) * (nint2 / 2)
b = (3 * nint1) + nreal
c = nreal**3
print(f'O produto do dobro do primeiro com metade do segundo é igual á {a}')
print(f'A soma do triplo do primeiro com o terceiro é igual á {b}')
print(f'O terceiro elevado ao cubo é igual á {c:.2f}')
