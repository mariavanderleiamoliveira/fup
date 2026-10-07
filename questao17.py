n1_texto = input('digite o primeiro numero: ')
n2_texto = input('digite o segundo numero: ')

n1 = int(n1_texto)
n2 = int(n2_texto)

if n1 == n2:
    print('numeros iguais')

elif n1 < n2:
    print(f'{n1} é menor que o {n2}')

else:
    print(f'{n2} é menor que o {n1}')