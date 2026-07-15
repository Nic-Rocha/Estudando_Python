'''
Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs. Depois, calcule e mostre a quantidade de produtos doces e amargos.
'''
produtos_alimenticios_impar = []
produtos_alimenticios_par = [] 
produtos_alimenticios_gerais = []
id = input('Digite 10 IDs de produtos alimentícios: ')
produtos_alimenticios_gerais = id.split()
for i in produtos_alimenticios_gerais:
  if int(i) % 2 == 0:
    produtos_alimenticios_par.append(i)
  else:
    produtos_alimenticios_impar.append(i)

print(f''' 
=== Produtos alimentícios ===
quantidade ímpar: {len(produtos_alimenticios_impar)}
quantidade par: {len(produtos_alimenticios_par)}
 ''')