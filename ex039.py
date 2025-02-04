from datetime import date

atual = date.today().year
nasc =  int(input('Ano de nascimento: '))
idade = atual - nasc
print('Você possui {} anos. '.format(idade))

if idade == 17:
    print('Você DEVE se alistar esse ano: ')
elif idade < 17:
    rest = 17 - idade
    print('Você ainda está novo para se alistar, espere {} ano(s)'.format(rest))

else:
    rest = idade - 17
    print('Você tem {} ano(s) a mais da idade de alistamento, não pode se alistar'.format(rest))

