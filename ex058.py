# Melhore o jogo DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

#import random

# computador = random.randint(0, 11) # Faz o computador 'pensar'
# computador = str(computador)
# print('-=-' * 20)
# print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
# print('-=-' * 20)
# jogador = input('Em que número eu pensei? ')  # Jogador tenta adivinhar
# print('PROCESSANDO...')
# while jogador not in computador:
#     jogador = input('Você errou! Em que número eu pensei? ')  # Jogador tenta adivinhar
# print('PARABÉNS! Você conseguiu me vencer!')



from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10. ')
print('Será que você consegue acertar qual foi? ')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente mais uma vez. ')
        elif jogador > computador:
            print('Menos... Tente mais uma vez. ')
print('Acertou!')
print('Você precisou de {} tentativas. Parabéns!'.format(palpites))




