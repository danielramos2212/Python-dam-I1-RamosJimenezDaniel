# Solicitar al usuario la temperatura en grados Kelvin
kelvin = float(input("Ingresa la temperatura de tu ciudad en grados Kelvin: "))

# Convertir a Celsius y Fahrenheit
celsius = kelvin - 273.15
fahrenheit = (kelvin - 273.15) * 9/5 + 32

#apartdos adicionales
# Determinar si la temperatura es calurosa, fría o está bien
if celsius >= 30:
    estado = "calurosa"
elif celsius <= 15:
    estado = "fría"
else:
    estado = "está bien"

# Mostrar resultados
print(f"Temperatura en Celsius: {celsius:.2f}°C")
print(f"Temperatura en Fahrenheit: {fahrenheit:.2f}°F")
print(f"La temperatura es {estado}.")