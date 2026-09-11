n1_texto = input('digite um numero do teclado ')

n1 = int(n1_texto)

print(f'voce digitou o numero {n1}')

resto = n1 % 2

if resto == 0:
    print('voce digitou um numero par')
else:
    print('voce digitou um numero impar')