#Faça um programa que peça o tamanho de um arquivo para download (em MB) e a
#velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado
#de download do arquivo usando este link (em minutos).

tamanho_arquivo = float(input('Digite o tamanho do arquivo: MB '))
velocidade_link = float(input('Digite a valocidade do link da internet: Mbps '))
tempo = (tamanho_arquivo/velocidade_link) / 60
print(f'O tempo para o arquivo ser baixado é {tempo:.2f} minutos')
