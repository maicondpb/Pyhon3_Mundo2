# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.

# nascimento = int(input('Digite seu ano de nascimento: '))
# idade = 2022 - nascimento
# print('Quem nasceu em {} tem {} anos em 2022'.format(nascimento, idade))

# if idade < 18:
#     print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - idade))
#     print('Seu alistamento será em {}.'.format(2022 + (18 - idade)))

# elif idade > 18:
#     print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))
#     idade1 = idade - 18
#     print('Seu alistamento foi em {}.'.format(2022 - idade1))

# elif idade == 18:
#     print('Você deve se alistar IMEDIATAMENTE!')

from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, atual))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')

elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos. Ainda faltam {} ano(s) para o alistamento.'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}.'.format(ano))

elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}.'.format(ano))





