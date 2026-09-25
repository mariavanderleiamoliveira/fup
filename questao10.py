saque_texto = input('quanto voce deseja sacar? ')

saque = int(saque_texto)

if saque >= 0:
    quantidade = saque // 200
    print(f'{quantidade} notas de 200')
    saque = saque % 200

if saque >= 0:
    quantidade = saque // 100
    print(f'{quantidade} notas de 100')
    saque = saque % 100

if saque >= 0:
    quantidade = saque // 50
    print(f'{quantidade} notas de 50')
    saque = saque % 50

if saque >= 0:
    quantidade = saque // 20
    print(f'{quantidade} notas de 20')
    saque = saque % 20

if saque >= 0:
    quantidade = saque // 10
    print(f'{quantidade} notas de 10')
    saque = saque % 10

if saque >= 0:
    quantidade = saque // 5
    print(f'{quantidade} notas de 5')
    saque = saque % 5

if saque >= 0:
    quantidade = saque // 2
    print(f'{quantidade} notas de 2')
    saque = saque % 2