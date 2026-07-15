'''
Em uma empresa de venda de imóveis você precisa criar um código que analise os dados de vendas anuais para ajudar a diretoria na tomada de decisão. O código precisa coletar os dados de quantidade de venda durante os anos de 2022 e 2023 e fazer um cálculo de variação percentual. A partir do valor da variação, deve ser enviada às seguintes sugestões:
Para variação acima de 20%: bonificação para o time de vendas. Para variação entre 2% e 20%: pequena bonificação para time de vendas. Para variação entre 2% e -10%: planejamento de políticas de incentivo às vendas. Para variação abaixo de -10%: corte de gastos.

'''
print('ANALISE DE VENDAS ANUAIS')
vendas_1 = float(input('Digite a quantidade de vendas no ano passado: '))
vendas_2 = float(input('Digite a quantidade de vendas no ano atual: '))

calculo = (vendas_2 - vendas_1) / vendas_1 * 100

if calculo > 20:
  print(f'''
 BONIFICAÇÃO DE VENDAS! 
 Variação: {calculo:.2f}%
 Vendas ano base: {vendas_1}
 Vendas ano atual: {vendas_2}
  ''')
if calculo <= 20 and calculo > 2:
  print(f'''
 PEQUENA BONIFICAÇÃO DE VENDAS. 
 Variação: {calculo:.2f}%
 Vendas ano base: {vendas_1}
 Vendas ano atual: {vendas_2}
  ''')
if calculo <= 2 and calculo > -10:
  print(f'''
 PLANEJAMENTO DE POLÍTICAS DE INCENTIVO ÀS VENDAS. 
 Variação: {calculo:.2f}%
 Vendas ano base: {vendas_1}
 Vendas ano atual: {vendas_2}
  ''')
if calculo <= -10:
  print(f'''
 CORTE DE GASTOS. 
 Variação: {calculo:.2f}%
 Vendas ano base: {vendas_1}
 Vendas ano atual: {vendas_2}
  ''')