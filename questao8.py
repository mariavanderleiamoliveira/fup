salario_texto = input('digite o valor do salario: ')
vendas_texto = input('digite o total de vendas efetuadas: ')

salario = float(salario_texto)
vendas = float(vendas_texto)

comissao = vendas * 0.15

salario_final = salario + comissao

print(f'mostre o salario fixo {salario} e o salario com comissao {salario_final}')