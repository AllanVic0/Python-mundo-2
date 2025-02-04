from datetime import date

atual = date.today().year
nasc = int(input('Digite o ano do seu nascimento: '))
idade = atual - nasc

if idade <= 9:
    print('Você tem {} anos e está na categoria MIRIM'.format(idade))
elif idade <= 14:
    print('Você tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade <= 19:
    print('Você tem {} anos e está na categoria JÚNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e está na categoria SÊNIOR'.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER'.format(idade))