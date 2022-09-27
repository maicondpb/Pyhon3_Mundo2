# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

from time import sleep
import emoji
print('CONTAGEM REGRESSIVA PARA OS FOGOS!!!')
for h in range(10, -1, -1):
    print(h)
    sleep(1)
if h == 0:
    print('BEM VINDO ANO NOVO!!! {}'.format(emoji.emojize(':fireworks:')))


