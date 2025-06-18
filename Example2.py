# write your own function that transform an Array of objects, 
# which could contain objects that are also array of objects,
# into a single Array. your function must transform any given array input.
# The input is an array and the output should be an array.
#       Input                                     Output
#[1, 2, ["3", "4"]]                         : [1, 2, "3", "4"]
#[1, 2, [3, 4, [5, 6]]]                     : [1, 2,3, 4, 5, 6]
#[1, 2, ["a", "b", [5, 6]]]                 : [1, 2, "a", "b", 5, 6]
#[1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]    : [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def list_final(input_array):
    output_array = []
    
    def evaluar_list(arr):
        for item in arr:
            if isinstance(item, list): # evalua si es una lista
                evaluar_list(item)  # recursivo si es una lista
            else:
                output_array.append(item)  # agrega al elemento de salida si no es una lista
    
    evaluar_list(input_array) # inicializa la funcion recursiva
    return output_array # retorna el array evaluado

# Ejemplo de uso:
array1 = [1, 2, ["3", "4"]]
final1 = list_final(array1)
print(final1)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]

array2 = [1, 2, [3, 4, [5, 6]]] 
final2 = list_final(array2)
print(final2)  # Output: [1, 2, 3, 4, 5, 6]

array3 = [1, 2, ["a", "b", [5, 6]]]
final3 = list_final( array3 ) # Output: [1, 2, "a", "b", 5, 6]
print(final3)  # Output: [1, 2, "a", "b", 5, 6]

array4 = [1, 2, [3, 4, [5, 6, [7, 8, [9, 10]]]]]
final4 = list_final(array4)
print(final4)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]