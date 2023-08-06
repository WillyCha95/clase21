"""
Leer dos variables N1 y N2. Ver si N1 es positivo, si lo es elevarlo
al cuadrado e imprimir el resultado. Y si N1 es 0 ó negativo sumarlo a N2 y entonces elevar al cuadrado la suma para imprimir el resultado
"""

N1 = int(input("Valor para N1: "))
N2 = int(input("Valor para N2: "))

if (N1 > 0):
    print("El cuadrado de N1 es", N1**2)

else: #if (N1 == 0 or N1 < 0):
    suma = N1 + N2 
    suma = suma**2
    print("El valor de la suma (al cuadrado) es de", suma)