valor = float(input('Qual o valor das compras? R$ '))
print('''Escolha entre as opções de pagamento abaixo
      1- à vista dinheiro/cheque: 10% de desconto
      2- à vista no cartão: 5% de desconto
      3- em até 2x no cartão: preço formal
      4- 3x ou mais no cartão: 20% de juros''')
opçpg = int(input('Escolha a opção de pagamento: '))

if opçpg == 1:
      desc = (valor * 10) / 100
      nvalor = valor - desc
      print('O valor a ser pago é de R$ {}'.format(nvalor))
elif opçpg == 2:
      desc = (valor * 5) / 100
      nvalor = valor - desc
      print('O valor a ser pago é de R$ {}'.format(nvalor))
elif opçpg == 3:
      print('O valor a ser pago é de R$ {}'.format(valor))
elif opçpg == 4:
      juros = (valor * 20) / 100
      nvalor = valor + juros
      print('O valor a ser pago é de R$ {}'.format(nvalor))
else:
      print('Opção inválida')