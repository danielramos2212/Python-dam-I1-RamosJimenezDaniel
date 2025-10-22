from datetime import datetime

# Solicita al usuario su nombre y año de nacimiento, calcula la edad y clasifica el tramo de edad.

# Solicitar el nombre
nombre = input("Introduce tu nombre: ")

# Solicitar el año de nacimiento y manejar errores si no es un número
while True:
    anio_nacimiento = input("Introduce tu año de nacimiento: ")
    try:
        anio_nacimiento = int(anio_nacimiento)
        break
    except ValueError:
        print("Por favor, introduce un año válido (número).")

# Calcular la edad actual
anio_actual = datetime.now().year
edad = anio_actual - anio_nacimiento

# Clasificar el tramo de edad
if edad < 18:
    tramo = "Menor de 18"
elif 18 <= edad <= 65:
    tramo = "Entre 18 y 65"
else:
    tramo = "Mayor de 65"

# Mostrar los resultados
print(f"\nNombre: {nombre}")
print(f"Edad: {edad}")
print(f"Tramo de edad: {tramo}")