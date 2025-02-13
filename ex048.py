soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c # podendo ser substituido por soma += c
print('O total da soma de todos {} os números multiplos de 3 é: {}'.format(cont, soma))