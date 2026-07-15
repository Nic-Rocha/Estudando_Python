#Vamos entender a distribuição de idades de pensionistas de uma empresa de previdência. Escreva um programa que leia as idades de uma quantidade não informada de clientes e mostre a distribuição em intervalos de [0-25], [26-50], [51-75] e [76-100]. Encerre a entrada de dados com um número negativo.
p_0_25 = 0
p_26_50 = 0
p_51_75 = 0
p_76_100 = 0

while True:
  idade = int(input('Digite a idade do pensionista( número negativo para encerrar):'))
  if idade >=0 and idade <= 25:
    p_0_25 += 1
    print(f'Pensionistas entre 0 e 25 anos. Total de pensionistas nesta idade até agora: {p_0_25}')
  if idade >= 26 and idade <= 50:
    p_26_50 += 1
    print(f'Pensionistas entre 26 e 50 anos. Total de pensionistas nesta idade até agora: {p_26_50}')

  if idade >= 51 and idade <= 75:
    p_51_75 += 1
    print(f'Pensionistas entre 51 e 75 anos. Total de pensionistas nesta idade até agora: {p_51_75}')
  
  if idade >= 76 and idade <= 100:
    p_76_100 += 1
    print(f'Pensionistas entre 76 e 100 anos. Total de pensionistas nesta idade até agora: {p_76_100}')

  if idade > 100:
    print('Idade inválida! Digite uma idade entre 0 e 100 ou um número negativo para encerrar o programa.')
    continue

  if idade < 0:
    print('Programa encerrado!')
    break

