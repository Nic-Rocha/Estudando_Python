'''
O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa. Para isso, foram fornecidos os seguintes dados:
{'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
 'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
 'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
 'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor, a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.
'''
idades_por_setor = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}
media_idades = {setor: sum(idades) / len(idades) for setor, idades in idades_por_setor.items()}
idade_media_geral = sum(media_idades.values()) / len(media_idades)
pessoas_acima_da_media = sum(1 for idades in idades_por_setor.values() for idade in idades if idade > idade_media_geral)

print("Média de idade por setor:")
for setor, media in media_idades.items():
    print(f"{setor}: {media:.2f} anos") 

print(f"\nIdade média geral: {idade_media_geral:.2f} anos")
print(f"\nNúmero de pessoas acima da idade média geral: {pessoas_acima_da_media}")    