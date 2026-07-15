 #Um programa deve ser escrito para ler dois números e, em seguida, perguntar à pessoa usuária qual operação ele deseja realizar. O resultado da operação deve incluir informações sobre o número - se é par ou ímpar, positivo ou negativo e inteiro ou decimal.

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
print('''
=== OPERÇÕES DESEJADAS ===
1- Soma
2- Subtração
3- Multiplicação
4- Divisão
5- Exponenciação
6- Resto da divisão
7- Sair
''')
op = input('Digite a operação desejada: ')

if op =='1':
  valor = n1 + n2
  print(f'A soma desses números é igual a {valor:.2f}')

elif op == '2':
  valor = n1 - n2
  print(f'A subtração desses números é igual a {valor:.2f}')

elif op == '3':
  valor = n1 * n2
  print(f'A multiplicação desses números é igual a {valor:.2f}')

elif op == '4':
  valor = n1 / n2
  print(f'A divisão desses números é igual a {valor:.2f}')

elif op == '5':
  valor = n1 ** n2
  print(f'A exponenciação desses números é igual a {valor:.2f}')

elif op == '6':
  valor = n1 % n2
  print(f'O resto da divisão desses números é igual a {valor:.2f}')

elif op == '7':
  valor = None
  print('Saindo...')
else:
  valor = None
  print('Opção inválida. Tente novamente.')

if valor is not None:
  if valor % 2 == 0:
    print(f'É um número par')
  else:
    print(f'É um número ímpar')
  if valor > 0:
      print(f'É um número positivo')
  else:
      print(f'É um número negativo')
  if valor == int(valor):
        print(f'É um número inteiro')
  else:
        print(f'É um número decimal')