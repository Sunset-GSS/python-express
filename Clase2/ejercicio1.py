'''
Crear un programa que pida dos numeros
y obtenja como resultado cual de ellos es par
o si ambos lo son.
# Si son pares, mostrar el mensaje "Ambos son pares"
# Si uno es par y el otro impar, mostrar "Uno es par y el otro impar"
'''

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

if a % 2 == 0 and b % 2 == 0:
    print("Ambos son pares")
elif a % 2 == 0 or b % 2 == 0:
    print("Uno es par y el otro impar")