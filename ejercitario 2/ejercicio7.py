"""
Lee un número por teclado e indica si es divisible por 3. Si no lo es, también debemos indicarlo
"""

numero = int(input("Ingrese un numero: "))
if numero % 3 == 0:
    print("Es divisible por 3")
else:
    print("No es divisible por 3")