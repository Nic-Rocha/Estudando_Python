#Crie um programa que solicite à pessoa usuária digitar seu nome, idade e altura em metros, e imprima na tela uma mensagem com essas informações. Exemplo: "Olá, meu nome é [nome], tenho [idade] anos e [altura] metros de altura."
nome = input('Digite seu primeiro nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite sua altura em cm: '))

print('Seu nome é %s %s, tem %d anos e %d cm de altura.' %(nome, sobrenome, idade, altura))