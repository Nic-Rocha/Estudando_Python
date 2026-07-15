#Colete novamente 5 inteiros e imprima a lista em ordem inversa à enviada.

numeros = [12, 112, 34, 45343,45645,65465, 3, 54, 65, 23, 83, 87, 21, 97,345, 213, 34, 675]

for i in numeros[0:5]:
  numeros.sort(reverse=True)
  print(i)