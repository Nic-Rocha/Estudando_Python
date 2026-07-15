#Calculando com operadores matemáticos

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a soma dos dois valores.
nu_01 = float(input('Digite o primeiro número: '))
nu_02 = float(input('Digite o segundo número: '))
Soma = nu_01 + nu_02
print(f'A soma desses números é igual a {Soma:.2f}')

#Crie um programa que solicite três valores numéricos à pessoa usuária e imprima a soma dos três valores.
valor1, valor2, valor3 = (input('Digite 3 números dando um espaço entre eles: ')).split()
valor1 = float(valor1)
valor2 = float(valor2)
valor3 = float(valor3)
soma = valor1 + valor2 + valor3
print(f'A soma desses números é igual a {soma:.2f}')

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a subtração do primeiro pelo o segundo valor.
Valor1, Valor2 = map(float, input('Digite dois números para a subtração: ').split())
print(f'A subtração desses números é igual a {Valor1 - Valor2:.2f}')

#Crie um programa que solicite dois valores numéricos à pessoa usuária e imprima a multiplicação dos dois valores.
n_1, n_2 = map(float, input('Digite dois valores númericos que queira multiplicar: ').split())
multi = n_1 * n_2
print(f'A multiplicação desses números é igual a {multi:.2f}')

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e realize a divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
V1, V2 = input('Escreva um numerador e um denominador: ').split()
div = float(V1) / float(V2)
print("%.1f ÷ %.1f = %.2f" %(float(V1), float(V2), div))

#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
V1, V2 = input('Escreva um numerador e um denominador(não pode ser 0): ').split()
if V2 == '0':
  print('O denominador não pode ser zero. Tente novamente.')
else:
  divisao = float(V1) / float(V2)
  print("%.1f ÷ %.1f = %.2f" %(float(V1), float(V2), divisao))

#Crie um programa que solicite dois valores numéricos, um operador e uma potência, e realize a exponenciação entre esses dois valores.
v1, v2 = input('Escreva o valor do operador e da potência escolhida: ').split()
v1, v2 = int(v1), int(v2)
exponenciacao = v1 ** v2
print(f'{v1} ^ {v2} = {exponenciacao}')

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador e realize a divisão inteira entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input('Digite o valor do numerador: '))
while True:
  denominador = int(input('Digite o valor do denominador (Não pode ser zero): '))
  if denominador == 0:
    print('O denominador não pode ser zero. Tente novamente.')
    continue
  else:
    break

divisao = numerador / denominador
print(f'{numerador} / {denominador} = {divisao:.2f}')

#Crie um programa que solicite dois valores numéricos, um numerador e um denominador, e retorne o resto da divisão entre os dois valores. Deixe claro que o valor do denominador não pode ser 0.
numerador = int(input('Digite o valor do numerador: '))
while True:
  denominador = int(input('Digite  o denominador(diferente de zero: )'))
  if denominador == 0:
    print('Zero não pode, digite outro valor.')
    continue
  else:
    break
resto = numerador % denominador
print(f'O resto da divisão é {resto:.2f}')