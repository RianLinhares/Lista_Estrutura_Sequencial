#Faça um Programa que pergunte quanto você ganha por hora e o
#número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

ganho_horas = float(input('Quanto você ganha por hora? R$  '))
horas = float(input('Quantas horas você trabalha por mês? '))
salario = ganho_horas * horas
print(f'''Com {horas} horas trabalhadas por mês, e um ganho de
{ganho_horas} R$ por hora, seu salário no final do mês será de {salario} R$''')
