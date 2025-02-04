n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))

media = (n1 + n2) / 2
print(media)

if media >= 5 and media < 7:
    print('Recuperação')
elif media < 5:
    print('Reprovado!')
elif media >= 7:
    print('Aprovado!!')