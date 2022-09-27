# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua caregoria, de acordo com a idade:
# Até 9 anos,: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('O atleta que nasceu em {} tem atualmente {} anos.'.format(nascimento, idade))
if idade <= 9:
    print('E sua categoria é MIRIM.')
elif idade <= 14:
    print('E sua categoria é INFANTIL.')
elif idade <= 19:
    print('E sua categoria é JÚNIOR.')
elif idade <= 25:
    print('E sua categoria é SÊNIOR.')
elif idade > 25:
    print('E sua categoria é MASTER.')



