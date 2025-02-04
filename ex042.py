sgm1 = float(input('Primeiro segmento: '))
sgm2 = float(input('Segundo segmento: '))
sgm3 = float(input('Terceiro segmento: '))

print('Os segmentos foram {}, {}, {}'.format(sgm1, sgm2, sgm3))

if sgm1 + sgm2 > sgm3 and sgm2 + sgm1 > sgm3 and sgm3 + sgm1 > sgm2:
    print('É possível formar um triângulo')
else:
    print('Não é possível formar um triângulo')

if sgm1 == sgm2 and sgm2 == sgm3 and sgm1 == sgm3:
    print('Forma-se um triângulo EQUILÁTERO')
elif sgm1 != sgm2 and sgm2 != sgm3 and sgm1 != sgm3:
    print('Forma-se um triângulo ESCALENO')
else:
    print('Forma-se um triângulo ISÓSCELES')