"""
Leer un número cualquiera y emitir el siguiente mensaje nulo(si es
cero), o positivo o negativo según sea el valor del número
"""

numero = int (input("Ingresa un numero: "))
if (numero == 0):
    print("El numero es nulo")
if (numero < 0):
    print("Es un numero negativo")
elif (numero > 0):
    print("El numero es positivo")



