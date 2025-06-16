# Escriba una funcion que determine si dos palabras son anagramas, 
# dos palabras son anagramas si tienen las exactas mismas letras aunque no en el mismo orden.

def son_anagramas(palabra1, palabra2):
    # Eliminar espacios y convertir a minúsculas
    palabra1 = palabra1.replace(" ", "").lower()
    palabra2 = palabra2.replace(" ", "").lower()
    # Comparar las letras de ambas palabras
    return sorted(palabra1) == sorted(palabra2)

# Ejemplo de uso
print(son_anagramas("espada","pesada")) # True
print(son_anagramas("hola", "cola")) # False
print(son_anagramas("amor", "roma"))  # True
print(son_anagramas("piedras","pietras")) #False