# cont = 1
# while True:
#     print(cont, ' -> ', end='')
#     cont += 1
# print('Acabou')

# n = soma = 0
# while n != 999:
#     n = int(input('Digite um número: '))
#     soma += n
# print('A soma vale {}'.format(soma))


n = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
print(f'A soma vale {soma}')


nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome:^20} tem {idade} anos e ganha R${salario:.2f}')


