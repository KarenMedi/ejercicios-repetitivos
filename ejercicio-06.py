# Calcular la cantidad de hombres y mujeres presentes en un salón de clases con un
# total de n personas
import random

hombre = 0
mujer = 0

for i in range(35):
    sexo = random.choice(['hombre', 'mujer'])

    if sexo == 'hombre':
        hombre += 1
    else: 
        mujer += 1

print(f'Hay {hombre} hombres en el salon')
print(f'Hay {mujer} mujeres en el salon')

