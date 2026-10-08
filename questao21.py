l1_texto = input('digite o primeiro lado')
l2_texto = input('degite o segundo lado')
l3_texto = input('digite o terceiro lado')

l1 = int(l1_texto)
l2 = int(l2_texto)
l3 = int(l3_texto)

l1_eh_lado_de_triangulo = l1 < l2 + l3
l2_eh_lado_de_triangulo = l2 < l1 + l3
l3_eh_lado_de_triangulo = l3 < l1 + l2

eh_um_triangulo = l1_eh_lado_de_triangulo and l2_eh_lado_de_triangulo and l3_eh_lado_de_triangulo

if eh_um_triangulo:
    if l1 == l2 and l2 == l3:
        print("trata-se de um triangulo equilatero")
    if l1 == l2 or l1 == l3 or l2 == l3:
        print('trata-se de um triangulo isoceles')
    else:
        print('trata-se de um triangulo escaleno')
else:
    print("nao sao lados de um triangulo")