#Escreva um programa para calcular quantos dias levará para a colônia de uma bactéria A ultrapassar ou igualar a colônia de uma bactéria B, com base nas taxas de crescimento de 3% e 1,5% respectivamente. Considere que a colônia A inicia com 4 elementos e a B com 10.

dias = 0
pop_a = 4
pop_b = 10
taxa_a = 0.03 
taxa_b = 0.015

while pop_a < pop_b:
        pop_a = pop_a + (pop_a * taxa_a)
        pop_b = pop_b + (pop_b * taxa_b)

print("Levou", dias, "dias para A alcançar ou ultrapassar B.")
print("População final de A:",(pop_a, 2))
print("População final de B:",(pop_b, 2))