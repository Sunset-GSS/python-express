'''
Ejemplo de estructura de control for
'''
# Ejemplo 1
#contador = 10
#for i in range(10):
#   print("El valor de i es:", i)

# Ejemplo 2
#for i in range(10): # Itera desde 0 hasta 9
#   print("El valor de i es:", i)


# Ejemplo de for con una lista
array = ["futbol", "pc", 18.6, 18,[6, 7, 10, 14], True, False]
print(len(array))
array.append("pc2") # Añadir un nuevo elemento al final de la lista

print(len(array)) # Longitud de la lista
for i in range(len(array)): # Itera sobre los índices de la lista
    print("El valor del array es:", array[i]) # Acceso al elemento en la posición i
print("Fin del bucle for con lista")
