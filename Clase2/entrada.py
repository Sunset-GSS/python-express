'''
Entrada de datos por teclado
'''
# Ejemplo 1: Usando input
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
cadena = nombre + " " + apellido
print("Hola ", cadena)

# Ejemplo 2: Usando f-strings
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
print("Nombre: ", nombre, "Apellido: ", apellido)
print(f"Nombre: {nombre} Apellido: {apellido}") # Mas estético

# Ejemplo 3: Usando format
cadena = input("Ingrese nombre de su proyecto: ")
print(f"El nombre de su proyecto es: {cadena}")

# Ejemplo 4: Usando int para convertir a número
numero = int(input("¿Qué versión es? "))
print(f"La versión del proyecto es: {numero+1}")