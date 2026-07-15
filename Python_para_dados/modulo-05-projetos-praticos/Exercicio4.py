#Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso, você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista. Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram, mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

print('=== INSITUTO DE METEOROLOGIA ===')
ano = input('Digite o ano: ')
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temperatura = []
for i in meses:
  temperatura.append(float(input(f'Digite a temperatura média do mês de {i}: ')))
media = sum(temperatura)/len(temperatura)

resultados_finais = {}
for i in range(len(temperatura)):
    if temperatura[i] > media:
        resultados_finais[meses[i]] = temperatura[i]

print(f''' === TEMPERATURAS DO ANO {ano} === 
Tempertaturas acima da média:43{resultados_finais}
media anual: {media:.2f}
''')