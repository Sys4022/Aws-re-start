

nombre_apellido =input(f"Cual es tu nombre completo: ")

edad=int(input(f"Que edad tienes: "))

edad2=edad+5

print(f""""""
)
print(f"Tu nombre completo es {nombre_apellido}")

print(f"Tu edad es {edad}")

print(f"En 5 años mas tendras {edad2}")

if edad>=18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print(f""""""
)
fruta=["manzana", "platano", "mango", "empanada","naranja"]

print(fruta)

print(f"La fruta que esta en la posicion 3 es {fruta[2]}")


print(f"""""")

number=int(input(f"inserta un numero: "))

if number %2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")

if number>=0:
    print("Tu numero es mayor a 0")
else:
    print("tu numero no es mayor a 0")
    
print(f"""""")

print("Good luck")
  
print("""""")
 
nombre = int(input("¿Cual es tu edad?: "))
 
if nombre <=18:
    print("Tu puedes votar")
elif nombre <=30:
    print("Esta permitido, cumpla su deber soldado")
elif nombre <=60:
    print("Gracias por todo, puede votar")
elif nombre <=80:
    print("Puede descansar soldado, a cumplido con su deber")
else:
    print("Todavia no puede votar")
    
print("""""")

celcius = int(input("Cuantos grados C° hacen: "))

if celcius <=0:
    print("El estado de la materia que se encuentra es Solido (Hielo)")
elif celcius <=100:
    print("El estado de la materia que se encuentra es Liquido")
elif celcius >=101:
    print("El estado de la materia que se encuentra es Gaseoso")
else: 
    print("El estado de la materia que sse encuentra es Desconocido")
    
print("""""")

numero_negativo = int(input("Que numero esta pensando: "))
    
if numero_negativo < 0:
    print("Su numero es negativo")
elif numero_negativo > 0: 
    print("Su numero es positivo")

else:
    print("El numero es cero(Neutro)")


# print("""""")
print("    Coloca 2 numeros" )
primero = int(input("El primer numero: "))
segundo = int(input("El segundo numero: "))

if primero>=0 and segundo >=0:
    print("Los 2 numeros son positivos")
    
elif primero<=0 and segundo <=0:
    print("Los dos numeros son negativos")
    
elif primero<=0 or segundo >=0:
    print("Uno de los numeros es negativo ")
    
elif primero>=0 or segundo <=0:
    print("Uno de los mumeros es negativo ")
    
else:
    print("vuelve a intentarlo")


print("""""")

edad = int(input("Introduce tu edad: "))
tiene_licencia = input("¿Tienes una identificacionpara votar? (True/False): ")


tiene_licencia = tiene_licencia.lower() == "true"


if edad >= 18 and tiene_licencia:
    print("Usted puede votar.")

elif not tiene_licencia:
    print("No puedes votar porque no tienes una identificacion.")

else:
    print("Usted no puede votar debido a su edad.")
print("""""")

