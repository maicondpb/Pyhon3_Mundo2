# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)
termo = int(input('Primeiro termo: '))
razao = int(input('Digite a razão: '))
décimo = termo + (10 - 1) * razao
for c in range(termo, décimo + razao, razao):
    print('{}'.format(c), end=' → ')
print('ACABOU')




