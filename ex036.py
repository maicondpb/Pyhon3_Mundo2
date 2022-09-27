# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valorcasa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o valor de seu salário: R$'))
tempo = int(input('Informe em quantos anos será pago a casa: '))
prestação = valorcasa / (tempo * 12)
print('Para pagar uma casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(valorcasa, tempo, prestação))
if prestação <= (salario * 30 / 100):
    print('O empréstimo foi concedido!')
else:
    print('O empréstimo foi negado!')



