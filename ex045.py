from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('O PC jogou {}'.format(itens[computador]))
jogador = randint(0, 2)
