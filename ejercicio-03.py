# Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
# Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
# de todo el grupo.
import random

#genera 20 calificaciones al azar y las asigna a una variable
calificaciones = [random.randint(1, 100) for i in range(1,21)]

#calcula el promedio de las notas
promedio = sum(calificaciones) / 20 

#calcula la calificacion mayor
calificacionMayor = max(calificaciones) 
#calcula la calificacion menor
calificacionMenor = min(calificaciones) 

print(f'La calificacion mayor es {calificacionMayor}')
print(f'La calificacion menor es {calificacionMenor}')
print(f'El promedio es {promedio}')



