# Python intuye el tipo de dato
# Para nombrar una variable debo asignar un valor así:
# identificador = valor

num = 2
num2 = 10

print(num) # son diferentes
print(num2)

# vemos el tipo de dato con type()
print(type(num)) # <class 'int'>

resultado = num + num2

print(resultado)


# Forma práctica de imprimir con variables
# Uso del f-string

print(f"Hola, sumé el valor {num} y el valor {num2} dando {resultado}")

### float : números decimales
### se separa el entero del decimal con punto

num = 4.5
num2 = 3.2

resultado = num * num2
print(f"Hola, multipliqué el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")

### complex : Complejo o imaginario
### se representa con una j al final del número
### Vienen del problema de raiz de menos 1

num = 4j
num2 = 2j

resultado = num - num2

print(f"Hola, resté el valor {num} y el valor {num2} dando {resultado}")
print(f"El tipo de dato de {num} es {type(num)}")


### Ejemplos de operaciones

num = 10

num2 = 5

suma = num + num2
resta = num - num2
mult = num * num2
division = num / num2 # Esto resultará en un float

# Hacer una división entera (omitiendo los decimales) con //
# NO aproxima, sólo elimina el decimal
division_entera = num // num2

print(division_entera)
# Residuo
# Se realizara una división, pero el resultado fuera lo que sobró
# de la división entera

modulo = num % 2

print(f"modulo: {num}  % 2 es {modulo}")

## Exponente: elevado **

elevado = 3 ** 2 

print(f"3 elevado a la 2 es {elevado}")