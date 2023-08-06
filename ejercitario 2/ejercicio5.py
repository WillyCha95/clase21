"""
Programa que se lea un número entero por teclado y se indique si el numero introducido es par o impar.
"""

numero = int(input("Por favor ingresa un numero: "))
if (numero % 2 == 0):
    print("Es un numero par")

if (numero % 2 == 1):
    print("Es un numero impar")