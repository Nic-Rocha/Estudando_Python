#Desenvolva um programa que leia um conjunto indeterminado de temperaturas em Celsius e informe a média delas. A leitura deve ser encerrada ao ser enviado o valor -273°C.

contador = 0
soma_temperaturas = 0

while True:
    temperatura = float(input("Digite a temperatura em Celsius (ou -273 para encerrar): "))
    if temperatura != -273 and temperatura > -273:
        soma_temperaturas += temperatura
        contador += 1
      
    else:
        media = soma_temperaturas / contador if contador > 0 else 0
        print(f'\nPROGRAMA ENCERRADO. A média das temperaturas informadas é: {media:.2f} °C')
        print(f'Foram informadas {contador} temperaturas válidas.')
        break
    
   