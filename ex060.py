# Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex: 5 != 5x4x3x2x1 = 120

# número = int(input('Digite um número para calcular seu Fatorial: '))
#
# resultado = 1
# count = 1
# while count <= número:
#     resultado *= count
#     count += 1
# print(resultado)

# from math import factorial
#
# número = int(input('Digite um número para calcular seu Fatorial: '))
# f = factorial(número)
# print('O fatorial de {} é {}'.format(número, f))

número = int(input('Digite um número para calcular seu Fatorial: '))
c = número
f = 1
print('Calculando {}! = '.format(número), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))


