'''
Escreva um programa que gere a tabuada de um número inteiro de 1 a 10, de acordo com a escolha da pessoa usuária. Como exemplo, para o número 2, a tabuada deve ser mostrada no seguinte formato:
Tabuada do 2:

2 x 1 = 2

2 x 2 = 4

[...]

2 x 10 = 20
'''
tabu = int(input('Digite o número que deseja a tabuada: '))
print(f'\n=== TABUADA DO {tabu} ===')
for tabuada in range(1,11):
  print(f'{tabu} x {tabuada} = {tabu * tabuada}')
