import math

raio_texto = input('digite o raio ')
altura_texto = input('digite a altura ')

altura = float(altura_texto)
raio = float(raio_texto)

volume = math.pi * raio * raio * altura
area = 2 * math.pi * raio * (altura + raio)

print(f'a area e {area} e o volume e {volume}')