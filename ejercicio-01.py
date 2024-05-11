# Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
# neutros.

negativos = 0
positivos = 0
neutros = 0

for i in range(-10, 11):
    if i < 0 :
        negativos += 1
    elif i == 0 :
        neutros += 1
    else:
        positivos += 1

print(f'{negativos} son negativos')
print(f'{positivos} son positivos')
print(f'{neutros} son neutros')