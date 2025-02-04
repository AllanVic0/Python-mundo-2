peso = float(input('Digite o seu peso (KG): '))
alt = float(input('Digite a sua altura (M): '))

imc = peso / (alt * alt)
print(imc)

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif imc > 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc > 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc > 30 and imc < 40:
    print('Você está obeso')
else:
    print('Você tem obesidade mórbida')