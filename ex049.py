tabuada = int(input('Digite um numero para saber a tabuada: '))
cont = 0
for c in range(1,11):
    cont += 1
    resultado = tabuada * c
    print('{} x {} = {}'.format(tabuada, cont, resultado))


# Versão do Guanabara
# num = int(input('Digite um numero para saber a tabuada: '))
# for c in range(1,11):
#     print('{} x {} = {}'.format(num, c, num*c))