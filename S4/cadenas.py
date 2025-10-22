# Solicitar una cadena al usuario
cadena = input("Introduce una cadena de caracteres: ")

vocales = "aeiouAEIOU"
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"

contador_vocales = 0
contador_consonantes = 0
contador_mayusculas = 0

for caracter in cadena:
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in consonantes:
        contador_consonantes += 1
    if caracter.isupper():
        contador_mayusculas += 1

total_caracteres = len(cadena)

print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Mayúsculas: {contador_mayusculas}")
print(f"Total de caracteres: {total_caracteres}")