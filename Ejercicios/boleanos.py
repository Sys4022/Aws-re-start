"""
    Tipo de dato primitivo
    
    Booleanos bools 
    
    Valor de verdad: True o False
    
"""

almuerzo = True
descanso = False

print(f"La variable almuerzo tiene el valor {almuerzo} y es de tipo {type(almuerzo)}")

"""
Tipos de datos compuestos

Colecciones

"""

#### LISTA

"""
Es una colección ordenada de valores

* Se define con [] y separa sus elementos con ,
* Los elementos pueden ser de cualquier tipo de dato
personas = ["Anahi", "David", "Ariel", 34, True, False]

* Mantiene un orden (Vale la pena aclarar)
"""

personas = ["Anahi", "David", "Ariel"]
numeros = [100, 95, 82]

myFruitList = ["apple", "banana", "cherry"]


print(f"La lista de frutas es {myFruitList}")
print(f"El tipo de dato es {type(myFruitList)}")


# Si quiero imprimir un elemento (banana) debo hacerlo por su índice
print(f"El segundo elemento es {myFruitList[1]}")

# Un error típico es intentar acceder a un índice que no existe
#print(myFruitList[5])
# IndexError: list index out of range


# Puedo cambiar el valor de los elementos
# Quiero cambiar banana por coco (indice 1)
myFruitList[1] = "coco"

print(f"La nueva lista es {myFruitList}")


"""
TUPLA

Muy similar a la lista
Se define con corchetes redondos () y se separa con ,
NO es mutable

"""

myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# Para acceder a un elemento lo hago igual que la lista 
print(myFinalAnswerTuple[2])

#Diccionarios

#coleccion de valores guardados con un modelo llave valor 
#El diccionario se define con {} y elementos separados po ,
#Cada elemento se ve : valor 


persona = {"Nombre:": "Julian Vasquez", "Ciudad": "Santiago", "Edad": 26}

print(persona)
print(type(persona))

# La manera de eceder a un valor es por su llave
print(persona["Ciudad"])


# Puedo cambiar un valor 
persona["Ciudad"] = "Viña del Mar"
persona["Ciudad"] = input("Cuál es tu ciudad? ")

print(persona["Ciudad"] )


######################################

#Genera una lista de tu top  de canciones favoritas e imprime la primera y última canción

mi_lista="Thriller", "Billy Jean", "Beat It", "Smooth criminal", "Bad"

print(mi_lista[0], mi_lista[4])

#Ejercicio 
#Imprime un diccionario que contenga los colores de su ropa





