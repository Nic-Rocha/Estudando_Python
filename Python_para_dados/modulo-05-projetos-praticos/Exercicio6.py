'''
Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças. A pesquisa foi feita e o votos computados podem ser observados abaixo:

Tabela de votos da marca
Design 1 - 1334 votos
Design 2 - 982 votos
Design 3 - 1751 votos
Design 4 - 210 votos
Design 5 - 1811 votos

Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.
'''
pesquisa_design ={
  'design 1': 1334,
  'design 2': 982,
  'design 3': 1751,
  'design 4': 210,
  'design 5': 1811
}

votos_totais = sum(pesquisa_design.values())
design_vencedor = max(pesquisa_design, key=pesquisa_design.get)
porcentagem_votos = (pesquisa_design[design_vencedor] / votos_totais) * 100

print(f''' === Resultado da pesquisa de mercado ===
    O design vencedor foi o {design_vencedor}! Com {pesquisa_design[design_vencedor]} votos, correspondendo a {porcentagem_votos:.2f}% do total de votos.  
    ''')