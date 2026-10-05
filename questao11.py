valor_da_compra = input('digite o valor da compra: ')
valor_pago = input('valor recebido: ')

c = int(valor_da_compra)
v = int(valor_pago)


troco = v - c

if troco >= 0:
    quantidade = troco // 200
    print(f'{quantidade} notas de 200')
    troco = troco % 200

if troco >= 0:
    quantidade = troco // 100
    print(f'{quantidade} notas de 100')
    troco = troco % 100

if troco >= 0:
    quantidade = troco // 50
    print(f'{quantidade} notas de 50')
    troco = troco % 50

if troco >= 0:
    quantidade = troco // 20
    print(f'{quantidade} notas de 20')
    troco = troco % 20

if troco >= 0:
    quantidade = troco // 10
    print(f'{quantidade} notas de 10')
    troco = troco % 10

if troco >= 0:
    quantidade = troco // 5
    print(f'{quantidade} notas de 5')
    troco = troco % 5

if troco >= 0:
    quantidade = troco // 2
    print(f'{quantidade} notas de 2')
    troco = troco % 2