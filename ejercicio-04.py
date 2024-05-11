#solicita el numero a multiplicar 
valor = int(input('Que valor deseas multiplicar? ')) 

for i in range(1, 11):
    # Realiza la Multiplicacion
    result = valor * i 
    print(f'{valor} x {i} = {result}')