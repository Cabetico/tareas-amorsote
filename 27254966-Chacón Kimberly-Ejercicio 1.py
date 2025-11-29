"""
1- Crea un programa que solicite 3 números.
   Los números pueden ser enteros o reales
   y calcule la multplicación de los 3 números
   y lo muestre por pantalla  (10 pts)
"""
try: 
   valor1 = float(input("Ingrese el primer número: "))
   valor2 = float(input("Ingrese el segundo número: "))
   valor3 = float(input("Ingrese el tercer número: "))
   
   resultado = valor1 * valor2 * valor3

   print("El resultado de la multiplicación es:", resultado)
except ValueError:
   print("It has to be a number, no chars please!!!")
