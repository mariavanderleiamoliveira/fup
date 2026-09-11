A_texto = input('digite o valor de A: ')
B_texto = input('digite o valor de B: ')

auxiliar = A_texto
A_texto = B_texto
B_texto = auxiliar

print(f'o valor trocado de A é {A_texto} e B {B_texto}')