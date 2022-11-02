#Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre em graus Fahrenheit.
# F = (C × 9/5) + 32

temperatura_c = float(input('Digite a temperatura em graus Celsius: '))
temperatura_f = (temperatura_c * (9/5)) + 32
print(f'Convertendo para graus Fahrenheit, temoos {temperatura_f:.2f} F')
