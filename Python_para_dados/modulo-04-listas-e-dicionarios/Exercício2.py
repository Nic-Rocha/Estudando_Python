#Com os mesmos dados da questão anterior, defina quantas compras foram realizadas acima de 3000 reais e calcule a porcentagem quanto ao total de compras.

lista_gastos = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]
quantidade_compras = 0
for compras in lista_gastos:
  if compras > 3000:
    quantidade_compras += 1
    porcentagem = quantidade_compras / len(lista_gastos) * 100
print(f'''
Quantidade de compras acima de R$3000.00: {quantidade_compras}
A porcentagem de compras acima de R$ 3000,00: {porcentagem:.2f}%
''')