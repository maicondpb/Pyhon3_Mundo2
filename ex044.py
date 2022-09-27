# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS GUANABARA '))

preço = float(input('Digite o valor do produto: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque: 10% de desconto
[ 2 ] à vista no cartão: 5% de desconto
[ 3 ] 2x no cartão: preço normal
[ 4 ] 3x ou mais no cartão: 20% de juros''')
forma_de_pagamento = int(input('Digite a forma de pagamento: '))
if forma_de_pagamento == 1:
    print('O produto de valor R${:.2f} terá o valor final de R${:.2f}'.format(preço, preço - (preço * 10 / 100)))
elif forma_de_pagamento == 2:
    print('O produto de valor R${:.2f} terá o valor final de R${:.2f}'.format(preço, preço - (preço * 5 / 100)))
elif forma_de_pagamento == 3:
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(preço / 2))
    print('O produto ficará no mesmo valor')
elif forma_de_pagamento == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print('Sua comprá será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
    print('O produto de valor R${:.2f} terá o valor final de R${:.2f}'.format(preço, total))
else:
    print('Opção Inválida!')






