#Escreva um programa que peça à pessoa usuária três números que representam os lados de um triângulo. O programa deve informar se os valores podem ser utilizados para formar um triângulo e, caso afirmativo, se ele é equilátero, isósceles ou escaleno.

n1, n2, n3 = map(float, input('Digite 3 números colocando um espaço entre eles:').split())
if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
  if n1 == n2 == n3:
    print('É um triângulo equilátero')
  elif n1 == n2 or n1 == n3 or n2 == n3:
    print('É um triângulo isósceles')
  else:
    print('É um triângulo escaleno')
else:
  print('Não é um triângulo')