valor = int(input('Digite o valor a ser convertido: '))
print('''Escolha a opção de que formato você quer converter:
                1 - Binário
                2 - octal
                3 - hexadecimal''')

opç = int(input('Escolha a opção de conversão: '))

if opç == 1:
    print('A conversão do número inserido é {}'.format(bin(valor)))
elif opç == 2:
    print('A conversão do número inserido é {}'.format(oct(valor)))
elif opç == 3:
    print('A convesão do número inserido é {}'.format(hex(valor)))
else:
    print('Operação inválida')