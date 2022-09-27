# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18.5: Abaixo do Peso
# IMC de 18.5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 a 40: Obesidade

peso = float(input('Digite seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f} '.format(imc))
if imc < 18.5:
    print('E você está Abaixo do Peso')
elif imc < 25:
    print('E você está no Peso Ideal')
elif imc < 30:
    print('E você está com Sobrepeso')
elif imc < 40:
    print('E você está com Obesidade')
else:
    print('E você está com Obesidade Mórbida, cuidado!')

