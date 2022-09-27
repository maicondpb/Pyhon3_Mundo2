# Crie um programa que leia o nome e preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final mostre:
# A: qual é o total gasto na compra.
# B: quantos produtos custam mais de R$ 1.000
# C: qual é o nome do produtos mais barato

print('-=' * 40)
print('{:-^40}'.format(' LOJA SUPER BARATÃO '))
print('-=' * 40)
somacompra = 0
maiorquemil = 0
menorpreço = 0
cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    somacompra += preço
    if preço > 1000:
        maiorquemil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra foi de {somacompra:.2f}')
print(f'Temos {maiorquemil} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
print('{:-^40}'.format(' FIM DO PROGRAMA '))


