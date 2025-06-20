# La operación RotarIzquiera sobre un array de tamaño N cambia
# cada elemento del array una posición a la izquierda.
# Dado un entero D, rotar el arreglo tantas veces a la izquierda
# como lo indica D y regrese el resultado.
# Ejemplo
# entradas:
# D = 2
# Arr = [1,2,3,4,5]
# Salida
# después de 2 rotaciones, el resultado es
# ArrR = [3,4,5,1,2]
def rotar_izquierda(arr, d):
    n = len(arr)
    d = d % n  # Asegurarse de que D no sea mayor que N
    return arr[d:] + arr[:d]

# Ejemplo de uso:
arr = [1, 2, 3, 4, 5]
d = 2
result = rotar_izquierda(arr, d)
print(result)  # Output: [3, 4, 5, 1, 2]
