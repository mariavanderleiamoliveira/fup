quantidade = input('digite a quantidade de maça: ')

q = int(quantidade)

if q < 12:
    valor = 0.30 * q
    print(f'valor total da compra: {valor}')

else:
    valor = 0.25 * q
    print(f'valor total da compra: {valor}')