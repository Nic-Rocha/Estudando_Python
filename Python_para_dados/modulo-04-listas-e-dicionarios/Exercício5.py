#Faça um programa que, ao inserir um número qualquer, cria uma lista contendo todos os números primos entre 1 e o número digitado.

print('NÚMEROS PRIMOS ATÉ O NÚMERO DESEJADO\n')
n = int(input('Digite o número: '))
print(f'\nAqui a lista contendo os números pedidos')

for i in range(2,n):
  primo = True
  for j in range(2,i):
    if i % j == 0:
      primo = False
      break
  if primo:
    print(i)