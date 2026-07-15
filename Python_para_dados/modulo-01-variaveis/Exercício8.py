#Crie um código que solicita 3 notas de um estudante e imprima a média das notas.
while True:
  print('=== ESCOLHA A MATÉRIA ===')
  print('1 - Matemática')
  print('2 - Português')
  print('3 - História')
  print('4 - Geografia')
  print('5 - Inglês')
  print('6 - Espanhol')
  print('7 - Francês')
  print('8 - Sair')

  escolha = input('Digite a matéria escolhida: ')
  if escolha == "8":
        print("Saindo...")
        break

  elif escolha in('1', '2', '3', '4', '5', '6', '7'):

    while True:
      entrada = input('Digite suas 3 notas desta matéria:').split()

      if len(entrada) != 3:
        print("Você precisa digitar exatamente 3 notas! Tente novamente.")
        continue
      try:
        n1, n2, n3 = map(float, entrada)
        break
      except ValueError:
            print("As notas precisam ser números! Tente novamente.")
            continue

    n1 = n1 * 2
    n2 = n2 * 3
    n3 = n3 * 5

    peso_total = 2+3+5
    media = (n1 + n2 + n3) / peso_total

    materias = {
    '1': 'Matemática',
    '2': 'Português',
    '3': 'História',
    '4': 'Geografia',
    '5': 'Inglês',
    '6': 'Espanhol',
    '7': 'Francês',
}

    escolha = materias[escolha]

    if media >= 6:
        print(f'{escolha}\nAPROVADO! Sua nota total foi {media:.32f}')
    else:
        print(f'{escolha}\nREPROVADO! Sua nota total foi {media:.2f}')
    break
  else:
    print('Opção inválida. Tente novamente.')