# Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
# números.
total = 0

for i in range(-10, 0): #solicitud de 10 numeros negativos
    i *= -1 #convierte los numeros negativos a positivos
    total += i # suma los numeros
    print(i)  #muestra los numeros

print(f'La suma de los numeros es {total}') #muestra el total