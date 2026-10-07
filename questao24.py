classe = input("Digite a classe do consumidor (A, B ou C): ")
consumo = float(input("Digite o consumo em kWh: "))

if classe == "A":
    tarifa = 0.5
elif classe == "B":
    tarifa = 0.8
elif classe == "C":
    tarifa = 1.0
else:
    print("Classe inválida")
    tarifa = 0

VF = consumo * tarifa
ICMS = 0.3 * VF
VP = VF + ICMS

print("Valor do fornecimento: R$", VF)
print("ICMS: R$", ICMS)
print("Valor a pagar: R$", VP)