'''
As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time. O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos. Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]. O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento. Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.
'''
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
abonos = {}
for salario in salarios:
    abono = salario * 0.1
    if abono < 200:
        abono = 200
    abonos[salario] = abono

    total_gastos = sum(abonos.values())
    colaboradores_minimo = sum(1 for abono in abonos.values() if abono == 200)
    maior_abono = max(abonos.values())
    
print(f"Total de gastos com o abono: {total_gastos}")
print(f"Quantidade de colaboradores que receberam o abono mínimo: {colaboradores_minimo}")
print(f"Maior valor de abono fornecido: {maior_abono}")