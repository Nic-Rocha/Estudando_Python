#Escreva um programa que peça uma data informando o dia, mês e ano e determine se ela é válida para uma análise.
DATA = input('Digite a data no formato dd/mm/aaaa: ')
dia, mes, ano = DATA.split('/')
dia = int(dia)
mes = int(mes)
ano = int(ano)

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

dias_no_mes = 31
if mes in [4, 6, 9, 11]:
    dias_no_mes = 30
if mes == 2 and bissexto:
    dias_no_mes = 29
if mes == 2 and not bissexto:
    dias_no_mes = 28

if ano < 1:
    print('Ano inválido')
elif mes < 1 or mes > 12:
    print('Mês inválido')
elif dia < 1 or dia > dias_no_mes:
    print('Dia inválido')
else:
    print('Data válida!')