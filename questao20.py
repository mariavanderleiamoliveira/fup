n1_texto = input('digite o primeiro numero:')
n2_texto = input('digite o segundo mumero:')
n3_texto = input('digite o terceiro numero:')

n1 = int(n1_texto)
n2 = int(n2_texto)
n3 = int(n3_texto)

if n1 >= n2 and n1 >= n3:
    print(f'o maior numero é {n1}')

elif n2 >= n1 and n2 >= n3:
    print(f'o maior numero é {n2}')

else:
     print(f'o maior numero é {n3}')