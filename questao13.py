peso = input('digite o seu peso: ')
altura = input('digite a sua altura: ')

p = float(peso)
a = float(altura)

imc = p / (a ** 2.0)

print(f' seu imc é {imc}')

if imc < 18.5:
    print('abaixo do peso')

elif imc < 25:
    print('peso normal')

elif imc < 30:
    print('sobrepeso')

elif imc < 35:
    print('obesidade grau 1')

elif imc < 40:
    print('obesidade grau 2')

else:
    print('obesidade grau 3')