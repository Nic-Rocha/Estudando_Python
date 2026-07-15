'''
a escola foi passada uma lista com nomes de estudantes que foram aprovados por média no semestre, mas é preciso verificar se alguns nomes estão nessa lista para verificar se os dados estão corretos.
A lista distribuida pode ser observada abaixo:

lista = 'José da Silva, Maria Oliveira, Pedro Martins, Ana Souza, Carlos Rodrigues, Juliana Santos, Bruno Gomes, Beatriz Costa, Felipe Almeida, Mariana Fernandes, João Pinto, Luísa Nascimento, Gabriel Souza, Manuela Santos, Thiago Oliveira, Sofia Ferreira, Rafael Albuquerque, Isabella Gomes, Bruno Costa, Maria Martins, Rafaela Souza, Matheus Fernandes, Luísa Almeida, Beatriz Pinto, Mariana Rodrigues, Gabriel Nascimento, João Ferreira, Maria Albuquerque, Felipe Oliveira'

Os nomes que precisam ser verificados são os seguintes:
nome_1 = 'Mariana Rodrigues'
nome_2 = 'Marcelo Nogueira'
'''
nome_1 = 'Mariana Rodrigues'
nome_2 = 'Marcelo Nogueira'

lista = ['José da Silva', 'Maria Oliveira', 'Pedro Martins', 'Ana Souza', 'Carlos Rodrigues', 'Juliana Santos', 'Bruno Gomes', 'Beatriz Costa', 'Felipe Almeida', 'Mariana Fernandes', 'João Pinto', 'Luísa Nascimento', 'Gabriel Souza', 'Manuela Santos', 'Thiago Oliveira', 'Sofia Ferreira', 'Rafael Albuquerque', 'Isabella Gomes', 'Bruno Costa', 'Maria Martins', 'Rafaela Souza', 'Matheus Fernandes', 'Luísa Almeida', 'Beatriz Pinto', 'Mariana Rodrigues', 'Gabriel Nascimento', 'João Ferreira', 'Maria Albuquerque', 'Felipe Oliveira']

if nome_1 in lista:
  print(f'{nome_1} está na lista!')
else:
  print(f'{nome_1} não está na lista!')

if nome_2 in lista:
  print(f'{nome_2} está na lista!')
else:
  print(f'{nome_2} não está na lista!')