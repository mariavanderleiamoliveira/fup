n1_texto = input('digite um numero do teclado ')

n = int(n1_texto)
n = float(n1_texto)

if n > 0:
    print('voce digitou um numero positivo')
elif n == 0:
    print('numero igual a zero')
else:
    print('voce digitou um numero negativo')