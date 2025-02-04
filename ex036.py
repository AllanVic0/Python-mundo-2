valorimv = float(input('Qual o valor do imóvel? R$ '))
salario = float(input('Qual seu atual salário? R$ '))
anos = float(input('Em quantos anos pretende finalizar as parcelas? '))

meses = anos * 12
parc = (valorimv / meses)
porc = (30 * salario) / 100


if parc > porc:
    print('Você não está apto para esse empréstimo, pelo alto valor das parcelas {:.2f}'.format(parc))
else:
    print('Você está apto para esse empréstimo e as parcelas serão de {:.2f}'.format(parc))