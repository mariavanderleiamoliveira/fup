n1_texto = input('digite o primeiro numero:')
n2_texto = input('digite o segundo mumero:')
n3_texto = input('digite o terceiro numero:')

n1 = int(n1_texto)
n2 = int(n2_texto)
n3= int(n3_texto)

if n1<n2 and n1<n3:
    if n2>n3:
        print(f'a ordem dos numeros sao {n1}, {n2}, {n3}')

    elif n1<n3 and n3<n2:
        print(f'a ordem dos numeros sao {n1}, {n3}, {n2}')

elif n2<n1 and n1<n3:
    print(f' a ordem dos numeros sao {n2}, {n1},{n3}')

elif n2<n3 and n3<n1:
    print(f'a ordem dos numeros sao {n2}, {n3}, {n1}')

elif n3<n1 and n1<n2:
    print(f'a ordem dos numeros sao {n3}, {n1}, {n2}')

else:
    print(n3, n2, n1)