# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

# soma = 0
# for c in range(1, 7):
#     if c % 2 == 0:
#         soma = soma + c
#         print(c, end=' ')
# print('A soma de todos os {} valores solicitados é {}'.format(c, soma))

soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você informou {} números pares e a soma foi {}'.format(cont, soma))
