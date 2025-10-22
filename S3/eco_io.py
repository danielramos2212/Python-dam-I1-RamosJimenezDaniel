# eco_io.py
"""
Este script solicita al usuario que ingrese tres números, calcula la suma, la media y el número mayor entre ellos, y muestra los resultados de forma ordenada y legible en pantalla.
Notas:
- El formato '.2f' en las cadenas f-string se utiliza para mostrar los números con dos decimales, lo que mejora la presentación de los resultados.
"""

print("=== Calculadora de Números ===")
print("Por favor, ingresa tres números:")

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))

suma = num1 + num2 + num3
media = suma / 3
mayor = max(num1, num2, num3)

print("\n--- Resultados ---")
print(f"Suma total:     {suma:.2f}")
print(f"Media:          {media:.2f}")
print(f"Número mayor:   {mayor:.2f}")
print("------------------")
print("\n--- Paridad de los números ---")
print(f"Número 1 ({num1:.2f}): {'Par' if int(num1) % 2 == 0 else 'Impar'}")
print(f"Número 2 ({num2:.2f}): {'Par' if int(num2) % 2 == 0 else 'Impar'}")
print(f"Número 3 ({num3:.2f}): {'Par' if int(num3) % 2 == 0 else 'Impar'}")