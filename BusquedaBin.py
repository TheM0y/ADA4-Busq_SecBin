import time

def busqueda_binaria(lista, objetivo):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# Lista de ejemplo (ordenada)
numeros = [1, 2, 3, 4, 7, 9]
print(f"Lista de números: {numeros}")
buscado = int(input("Ingrese el número a buscar (binaria): "))

# Medir el tiempo de ejecución
inicio = time.time()
resultado = busqueda_binaria(numeros, buscado)
fin = time.time()

if resultado != -1:
    print(f"Número encontrado en la posición {resultado}")
else:
    print("Número no encontrado")

print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")
