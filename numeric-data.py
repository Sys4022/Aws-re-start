2 + 2

4 - 2













#asignacion de variable

myString="2"

print(f"El valor de mi variable es {myString} y su tipo es {type(myString)}")

#Operador
#NO puedo hacer directamente operaciones aritmeticas 

#concatecion
#union de dos o mas string

nombre="Nombre"
apellido="Apellido"

Nombre_completo= nombre + " " + apellido #es concatenacion

print(f"El nombre completo {Nombre_completo}") 


###Funcion de entrada por teclado 
# imput()
# frena el programa y espera que el usuario ingrese algo por teclado
#por defecto el valor que se recibe es de tipo string 
Nombre= input("ingresa el nombre: ")

Apellido = input("Ingresa tu apellido: ")

nombre_completo = Nombre + " " + Apellido 

print(f"Hola, tu nombre es {nombre_completo}")

# Conversion de tipos de vatiables
# Casting o casteo 

# Puedo concertir un string a int o float asi 

variable= "2"
numero_convertido = int(variable)
print(f"La variable era de tipo{type(variable)} y ahora es {type(numero_convertido)}")

"""
conversiones 

int()
float()
complex()
str()

"""

#Voy a sumar dos numeros 
#Si no convierto lo que recibo en input sera string
#convierto la entrada input a int
num = int(input("Ingresa un numero: "))#5
num2 = int(input("Ingresa otro número: ")) # 2

#al ser string se concatenaran (unen)
resultado =num + num2

print(f"La suma de {num} y {num2} es {resultado}")