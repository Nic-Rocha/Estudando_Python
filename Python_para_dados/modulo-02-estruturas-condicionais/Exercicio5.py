#Um estabelecimento está vendendo combustíveis com descontos variados. Para o etanol, se a quantidade comprada for até 15 litros, o desconto será de 2% por litro. Caso contrário, será de 4% por litro. Para o diesel, se a quantidade comprada for até 15 litros, o desconto será de 3% por litro. Caso contrário, será de 5% por litro. O preço do litro de diesel é R 2,00eopreçodolitrodeetanoléR  1,70. Escreva um programa que leia a quantidade de litros vendidos e o tipo de combustível (E para etanol e D para diesel) e calcule o valor a ser pago pelo cliente.

print('''  
=== TIPOS DE COMBUSTÍVEIS ===
1- Etanol
2- Diesel
''')
tipo = input('Digite o tipo de combustível desejado: ')
litros = float(input('Digite a quantidade de litros desejada: '))

if tipo == '1':
  if litros <= 15:
    desconto = 0.02
    print(f''' 
    === TOTAL ===
  tipo -> Etanol
  litros -> {litros}
  Valor final -> R$ {litros*1.70*(1-desconto):.2f}
    ''')
  else:
    desconto = 0.04
    print(f''' 
    === TOTAL ===
  tipo -> Etanol
  litros -> {litros}
  Valor final- R$ {litros*1.70*(1-desconto):.2f}
    ''')
elif tipo == '2':
  if litros <= 15:
    desconto = 0.03
    print(f''' 
    === TOTAL ===
  tipo -> Diesel
  litros -> {litros}
  Valor final -> R$ {litros*2*(1-desconto):.2f}
    ''')
  else:
    desconto = 0.05
    print(f''' 
    === TOTAL ===
  tipo -> Diesel
  litros -> {litros}
  Valor final -> R$ {litros*2*(1-desconto):.2f}
    ''')
else:
  print('Opção inválida. Tente novamente.')
