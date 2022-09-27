# Crie um programa que leia uma grase qualquer e diga se ela é um paçindromo, desconsiderando os espaços. Exemplos de palíndromos:
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA


# palavra = str(input('Digite uma palavra para verificar se ela é palíndromo ou não: ')).strip().upper()
# w = ''
# for c in palavra:
#     w = c + w
# if (palavra == w):
#     print('A palavra digitada é palíndroma!')
# else:
#     print('A palabra digitada não é palídroma!')

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('A palavra digitada foi {} e seu inverso é {}'.format(junto, inverso))
if inverso == junto:
    print('A frase digitada é palíndroma!')
else:
    print('A frase digitada não é palíndroma!')




