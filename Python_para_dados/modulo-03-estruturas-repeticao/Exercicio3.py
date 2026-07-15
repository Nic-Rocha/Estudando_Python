#Para tratar uma quantidade de 15 dados de avaliações de pessoas usuárias de um serviço da empresa, precisamos verificar se as notas são válidas. Então, escreva um programa que vai receber a nota de 0 a 5 de todos os dados e verificar se é um valor válido. Caso seja inserido uma nota acima de 5 ou abaixo de 0, repita até que a pessoa usuária insira um valor válido.
v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15 = map(int, input("Digite 15 notas de avaliação (de 0 a 5): ").split())

for i, nota in enumerate([v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13, v14, v15]):
    while nota < 0 or nota > 5:
        nota = int(input(f'Nota inválida para a avaliação. Digite uma nota válida (de 0 a 5): '))
        continue
    while nota >= 0 and nota <= 5:
        print(f'Nota {i+1}: {nota} é válida.')
        break
print("Todas as notas foram validadas com sucesso!")