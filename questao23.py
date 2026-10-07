import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

D = b**2 - 4*a*c

if D < 0:
    print("Não existem raízes reais.")

elif D == 0:
    x = -b / (2*a)
    print("Existe uma raiz real:")
    print("x =", x)

else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)

    print("Existem duas raízes reais diferentes:")
    print("x1 =", x1)
    print("x2 =", x2)                                                   