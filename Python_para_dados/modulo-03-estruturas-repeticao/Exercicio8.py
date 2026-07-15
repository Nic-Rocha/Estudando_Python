'''
Em uma eleição para gerência em uma empresa com 20 pessoas colaboradoras, existem quatro candidatos(as). Escreva um programa que calcule o(a) vencedor(a) da eleição. A votação ocorreu da seguinte maneira:

-Cada colaborador(a) votou em uma das quatro pessoas candidatas (querepresentamos pelos números 1, 2, 3 e 4).
-Também foram contabilizados os votos nulos (representados pelo número 5) e os votos em branco      (representados pelo número 6).

Ao final da votação, o programa deve exibir o número total de votos para cada candidato(a), os nulos e os votos em branco. Além disso, deve calcular e exibir a porcentagem de votos nulos em relação ao total de votos e a porcentagem de votos em branco em relação ao total de votos.
'''

candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
brancos = 0


total_colaboradores = 20


for i in range(total_colaboradores):
    voto = int(input(f"Digite o seu voto entre o candidato 1 ao 4 (podendo ser nulo ou em branco) {i+1}: "))

    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        brancos += 1
    else:
        print("Voto inválido!")


porcentagem_nulos = (nulos / total_colaboradores) * 100
porcentagem_brancos = (brancos / total_colaboradores) * 100

votos_candidatos = [candidato1, candidato2, candidato3, candidato4]
vencedor = votos_candidatos.index(max(votos_candidatos)) + 1

print("\n=== Resultado da Eleição ===")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")
print(f"Candidato 4: {candidato4} votos")
print(f"Votos nulos: {nulos}")
print(f"Votos em branco: {brancos}")
print(f"\nPorcentagem de votos nulos: {porcentagem_nulos:.2f}%")
print(f"Porcentagem de votos em branco: {porcentagem_brancos:.2f}%")
print(f"\nO(A) vencedor(a) da eleição foi o(a) Candidato(a) {vencedor}!")