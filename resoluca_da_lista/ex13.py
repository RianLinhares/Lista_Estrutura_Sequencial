#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input('Digite a altura da pessoa: [m]  '))
sexo = str(input('Qual o sexo da pessoas? [F/M] ')).upper()[0]
if sexo == 'M':
    peso_ideal = (72.7 * altura) - 58
    print(f'Com uma altura de {altura} m, peso ideal é {peso_ideal:.2f} kg')
elif sexo == 'F':
    peso_ideal = (62.1 * altura) - 44.7
    print(f'Com uma altura de {altura} m, peso ideal é {peso_ideal:.2f} kg')
else:
    print('Digito inválido tente novamente utilizando apenas F ou M')
