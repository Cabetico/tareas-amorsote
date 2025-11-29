"""
2-  Crea un programa que pida su nombre y su (primer) apellido al usuario, 
	A partir de estos datos, deberá crear una cadena que contenga el apellido, 
	una coma, 
	un espacio y el nombre, y deberá mostrarla en pantalla. 
	
	Por ejemplo, 
	
	Si el nombre es Nacho y el apellido es Cabanes 
	la cadena resultante será Cabanes, Nacho (10 pts)
"""
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su primer apellido: ")

resultado = apellido.upper() + ", " + nombre.upper()

print("Welcome:", resultado)