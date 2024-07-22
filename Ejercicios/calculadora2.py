"""
--- calculadora automatica 2 numeros ----

Vamos a solicitar al usuario 2 numeros 
y a realizar todas la operaciones posibles 
mostrando el resultado de una forma clara 
(+, *, -, /, //, %, **)
-----------------------------------------
"""
num = int(input("Ingresa un numero: "))#5
num2 = int(input("Ingresa otro número: ")) # 2

#Al ser string se concatenaran (unen)
suma =num + num2
multiplicacion =num * num2
division =num / num2
resta =num - num2
division_entera=num // num2
porcentaje =num % num2
potencia =num ** num2


###Todas las operaciones posibles de {num} y {num2}.")

print()
print("CALCULADORA AUTOMATICA CON 2 NUMEROS .")
print()

print("Resultados en con distintas operaciones:")
print()

print(f"Suma:            {num} +  {num2} = {suma}")
print(f"Multiplicacion:  {num} *  {num2} = {multiplicacion}")
print(f"Division:        {num} /  {num2} = {division}")
print(f"Resta:           {num} -  {num2} = {resta}")
print(f"Division Entera: {num} // {num2} = {division_entera}")
print(f"Porcentaje:      {num} %  {num2} = {porcentaje}")
print(f"Potencia:        {num} ^  {num2} = {potencia}")
