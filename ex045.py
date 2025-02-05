from random import randint

print('''JOKENPÔ
      [0] Pedra
      [1] Papel
      [2] Tesoura''')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

jogador = int(input('Faça sua jogada: '))

print('O PC jogou {}: '.format(itens[computador]))
print('O jogador jogou {}: '.format(itens[jogador]))

if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('Jogador venceu')
    elif jogador == 2:
        print('Computador venceu')
elif computador == 1:
    if jogador == 0:
        print('Computador venceu!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('Jogador venceu')
elif computador == 2:
    if jogador == 0:
        print('Jogador venceu!')
    elif jogador == 1:
        print('Computador venceu!')
    elif jogador == 2:
        print('EMPATE!')
else:
    print('Jogada inválida')
