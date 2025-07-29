'''
Ejemplos de listas en Python
'''

array = ["futbol", "pc", 18.6, 18,[6, 7, 10, 14], True, False]
print (array)

# Acceso a los elementos de la lista
print(array[0])  # Acceso al primer elemento
print(array[4]) # Acceso a la sublista
print(array[4][2]) # Acceso al tercer elemento de la sublista
print(array[0:3]) # Acceso a los primeros tres elementos de la lista
print(array[0:5:2]) # Acceso a los elementos de la lista con un paso de 2
print(array[-1]) # Acceso al último elemento de la lista

print(len(array)) # Longitud de la lista


# Modificar elementos de la lista
array.append("66") # Añadir un nuevo elemento al final de la lista
print(array)
array.insert(2, "cel") # Insertar un nuevo elemento en la posición 2
print(array)
array.extend(["notebook", "natacion", "tenis"]) # Añadir varios elementos al final de la lista
print(array)


# Eliminar elementos de la lista
array.remove("cel") # Eliminar el elemento "cel" de la lista
print(array)
array.pop() # Eliminar el último elemento de la lista
print(array)
array.pop(2) # Eliminar el elemento en la posición 2
print(array)
array.clear() # Limpiar la lista
print(array)


# Concatenar listas
array = ["futbol","tenis", "pc", 18.6, 18,[6, 7, 10, 14], True, False] # Volver a inicializar la lista
array2 = ["baloncesto", "natacion", "tenis"] # Crear una segunda lista
array3 = array + array2 # Concatenar las dos listas 
print(array3)

# Operaciones con listas
print("futbol" in array3) # Comprobar si un elemento está en la lista
print(array3.index("baloncesto")) # Obtener el índice del elemento "futbol"
print(array3.count("tenis")) # Contar cuántas veces aparece el elemento "tenis" en la lista


# Ordenar e invertir listas
array4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
array4.reverse() # Invertir el orden de los elementos de la lista
print(array4)
array5 = [1, 3, 2, 5, 4, 6, 8, 7, 10, 9]
array5.sort() # Ordenar los elementos de la lista
print(array5)
