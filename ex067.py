# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo.


while True:
    num = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 20)
    if num < 0:
        break
    for n in range(1, 11):
        print(' {} x {} = {}'.format(num, n, num*n))
    print('-' * 20)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
