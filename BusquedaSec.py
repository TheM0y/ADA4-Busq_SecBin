import time

def busqueda_secuencial(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

# Lista de ejemplo
numeros = [4, 2, 7, 1, 9, 3]
print(f"Lista de números: {numeros}")
buscado = int(input("Ingrese el número a buscar (secuencial): "))

inicio = time.time()
resultado = busqueda_secuencial(numeros, buscado)
fin = time.time()

if resultado != -1:
    print(f"Número encontrado en la posición {resultado}")
else:
    print("Número no encontrado")

print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
