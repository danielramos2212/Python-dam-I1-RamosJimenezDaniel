from collections import Counter
import re
# n.strip() elimina los espacios en blanco al inicio y al final de cada número ingresado por el usuario.
# Esto asegura que, aunque el usuario escriba espacios después de las comas, los números se procesen correctamente.
# Solicita al usuario 5 números separados por comas
#^ y $: Indican el inicio y el final de la cadena. Así, toda la cadena debe coincidir con el patrón.
#\s*: Permite cualquier cantidad de espacios en blanco al principio y al final.
#-?: Permite un signo negativo opcional antes del número.
#\d+: Uno o más dígitos (el número entero).
#(\.\d+)?: Un punto seguido de uno o más dígitos (la parte decimal), opcional.
#(\s*,\s*-?\d+(\.\d+)?){4}:
#\s*,\s*: Una coma, permitiendo espacios antes y después.
#-?\d+(\.\d+)?: Otro número (igual que antes).
#{4}: Esto debe repetirse exactamente 4 veces, para un total de 5 números (el primero más los 4 adicionales).
patron = r'^\s*-?\d+(\.\d+)?(\s*,\s*-?\d+(\.\d+)?){4}\s*$'
while True:
    entrada = input("Introduce 5 números separados por comas: ")
    if re.match(patron, entrada):
        break
    print("Formato incorrecto. Debes ingresar 5 números separados solo por comas.")

# Limpia espacios y convierte a lista de floats
numeros = [float(n.strip()) for n in entrada.split(",")]

# Calcula suma, media y máximo
suma = sum(numeros)
media = suma / len(numeros)
maximo = max(numeros)

print(f"Suma: {suma}")
print(f"Media: {media}")
print(f"Máximo: {maximo}")
minimo = min(numeros)
print(f"Mínimo: {minimo}")

# Detecta duplicados y cuenta repeticiones

contador = Counter(numeros)
duplicados = {num: rep for num, rep in contador.items() if rep > 1}

if duplicados:
    print("Números duplicados y sus repeticiones:")
    for num, rep in duplicados.items():
        print(f"{num} aparece {rep} veces")
else:
    print("No hay números duplicados.")
#a