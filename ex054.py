# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

# from datetime import date
# totatingiu = 0
# totnaoatingiu = 0
# for c in range(1, 8):
#     nascimento = int(input('Digite o ano da {}ª pessoa: '.format(c)))
#     atual = date.today().year
#     idade = atual - nascimento
#
#     if idade >= 18:
#         totatingiu += 1
#
#     else:
#         totnaoatingiu += 1
#
# print('{} pessoas atingiram a maioridade!'.format(totatingiu))
# print('{} pessoas não atingiram a maioridade!'.format(totnaoatingiu))

from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nascimento = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoa)))
    idade = atual - nascimento
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade '.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))

