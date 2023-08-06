"""
Un individuo desea invertir su capital en un banco y desea saber cuánto dinero ganará después de un mes,
si el banco paga a 2% de interés mensual.
"""

capital = int(input("Por favor ingrese su monto para el capital: "))
meses = int(input("Ingresa la cantidad de meses: "))
interes = 2 / 100
#al_mes = capital + (capital * interes) 
al_mes = capital * (1 + (interes * meses))
print("El capital, al cabo del mes, sera: ", al_mes)