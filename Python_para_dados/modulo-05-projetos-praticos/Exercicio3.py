'''
Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas. Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito. Cada questão vale um ponto e existem as alternativas A, B, C ou D.
Gabarito da prova:
01 - D
02 - A
03 - C
04 - B
05 - A
'''
print('=== PROVA DE GEOGRAFIA | VALENDO 5 ===')
nome = input('Digite seu nome: ')
print('''
Q1- Qual é o maior país do mundo em extensão territorial?
a) Canadá
b) Estados Unidos
c) China
d) Rússia
''')
resposta_q1 = input('Digite a alternativa correta: ')

print('''
Q2- Qual é a linha imaginária que divide a Terra em Hemisfério Norte e Hemisfério Sul?
a) Linha do Equador
b) Trópico de Câncer
c) Meridiano de Greenwich
d) Trópico de Capricórnio
''')
resposta_q2 = input('Digite a alternativa correta: ')

print('''
Q3- Qual é o maior planeta do sistema solar?
a) Vênus
b) Saturno
c) Júpiter
d) Urano
''')
resposta_q3 = input('Digite a alternativa correta: ')

print('''
Q4- Qual é o oceano mais profundo do mundo?
a) Atlântico
b) Pacífico
c) índico
d) Ártico
''')
resposta_q4 = input('Digite a alternativa correta: ')

print('''
Q5- Qual país tem a maior população do mundo atualmente?
a) Índia
b) China
c) Indonésia
d) Estados Unidos
''')
resposta_q5 = input('Digite a alternativa correta: ')

gabarito = {'01': 'd', '02': 'a', '03': 'c', '04': 'b', '05': 'a'}
respostas = {'01': resposta_q1, '02': resposta_q2, '03': resposta_q3, '04': resposta_q4, '05': resposta_q5}
nota = 0
for i in respostas:
    if respostas[i] == gabarito[i]:
        nota += 1

print(f''' ===NOTA FINAL===
Nome: {nome}
Nota: {nota}
''')