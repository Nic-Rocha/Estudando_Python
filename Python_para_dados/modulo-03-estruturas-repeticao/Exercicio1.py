#Escreva um programa que peça dois números inteiros e imprima todos os números inteiros entre eles.
n1, n2 = int(input("Digite o primeiro número inteiro: ")), int(input("Digite o segundo número inteiro: "))

if n1 < n2:
  for i in range(n1 + 1, n2):
      print(i)
elif n1 > n2:
  for i in range(n2 + 1, n1):
      print(i)
elif n1 == n2:
    print("Os números são iguais, não há números entre eles.")
else: 
    print("Entrada inválida. Por favor, insira números inteiros válidos.")