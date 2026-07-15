'''
Uma empresa de e-commerce está interessada em analisar as vendas dos seus produtos. Os dados das vendas foram armazenados em um dicionário:
{'Produto A': 300, 'Produto B': 80, 'Produto C': 60,
 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
'''
produtos = {'Produto A': 300, 'Produto B': 80, 'Produto C': 60, 'Produto D': 200, 'Produto E': 250, 'Produto F': 30}
total_vendas = sum (produtos.values())

produto_mais_vendido = None
maior_valor = 0

for produto, vendas in produtos.items():
    if vendas > maior_valor:
        maior_valor = vendas
        produto_mais_vendido = produto

print(f''' === RELATÓRIO DE VENDAS ===
Total de vendas: {total_vendas}
Produto mais vendido: {produto_mais_vendido}
''')