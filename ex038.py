valor1 = int(input('Digite o primeiro valor a ser comparado: '))
valor2 = int(input('Digite o segundo valor a ser comparado: '))

if valor1 > valor2:
    print('{} é maior que {}'.format(valor1, valor2))
elif valor2 > valor1:
    print('{} é maior que {}'.format(valor2, valor1))
else:
    print('Ambos o valores são iguais')