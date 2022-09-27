# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A: quantas pessoas tem mais de 18 anos.
# B: quantos homens foram cadastrados
# C: quantas mulheres tem menos de 20 anos.

tot18 = 0
sexomasc = 0
mulher20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        sexomasc += 1
    if sexo == 'F' and idade < 20:
        mulher20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('QUer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total de pessoas maiores de idade: {tot18}')
print(f'Total de homens foi: {sexomasc}')
print(f'Total de mulheres com menos de 20 anos foi de: {mulher20}')
