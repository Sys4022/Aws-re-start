
# 🌌 AWS Re/Start Python Exercises 🚀

## Bienvenido, joven Padawan 🧑‍🎓

En esta galaxia muy, muy lejana, te embarcarás en una aventura para dominar los fundamentos de Python. Estos ejercicios han sido diseñados por los Maestros de Generation para guiarte en tu camino hacia la maestría en la Fuerza de la programación. Que la Fuerza te acompañe. ✨

### ⚙️ Configuración del Entorno Cloud 9

Para comenzar tu viaje, primero debes configurar tu entorno Cloud 9 en AWS. Sigue estos pasos:

1. **Crear un Entorno Cloud 9**:
    - Navega a AWS Management Console.
    - Busca y selecciona **Cloud 9**.
    - Crea un nuevo entorno y dale un nombre como `python-training`.

2. **Configuración del Entorno**:
    - Selecciona un entorno **t2.micro** para un rendimiento óptimo y económico.
    - Configura el entorno con las herramientas necesarias para Python (ya preinstaladas en la mayoría de los casos).

### 🌟 Ejercicios Básicos de Python

A continuación, encontrarás una serie de ejercicios diseñados para mejorar tus habilidades en Python. Completa cada ejercicio en el orden proporcionado y consulta a tu mentor Jedi si tienes alguna duda.

#### 1. 🚀 Hola Mundo

Crea un programa que imprima "Hola, Mundo!".

```python
# hola_mundo.py
print("Hola, Mundo!")
```

#### 2. 🔢 Números y Operaciones

Escribe un programa que solicite al usuario dos números y luego imprima la suma, resta, multiplicación y división de esos números.

```python
# operaciones_basicas.py
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"División: {num1 / num2}")
```

#### 3. 🔄 Ciclos y Bucles

Crea un programa que imprima los números del 1 al 10 usando un bucle `while`.

```python
# bucle_while.py
i = 1
while i <= 10:
    print(i)
    i += 1
```

#### 4. 📜 Listas y Bucles

Escribe un programa que imprima cada elemento de una lista de nombres.

```python
# lista_nombres.py
nombres = ["Luke", "Leia", "Han", "Chewbacca", "Yoda"]

for nombre in nombres:
    print(nombre)
```

#### 5. 🎲 Adivina el Número

Desarrolla un juego simple donde el usuario tiene que adivinar un número entre 1 y 10 generado aleatoriamente por el programa.

```python
# adivina_numero.py
import random

numero_secreto = random.randint(1, 10)
intento = None

while intento != numero_secreto:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    if intento < numero_secreto:
        print("Muy bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Muy alto. Intenta de nuevo.")
    else:
        print("¡Correcto! Has adivinado el número.")
```

### 📝 Notas Finales

Recuerda, joven Padawan, la práctica y la perseverancia son tus mejores aliados en este viaje. Completa cada ejercicio y busca mejorar cada día. La Fuerza de Python es poderosa, y tú tienes el potencial para convertirte en un Maestro. Que la Fuerza te acompañe. 🌌

---

© 2024 Generation. All rights reserved.
```

Este README te proporcionará una guía básica para configurar tu entorno de desarrollo y comenzar con ejercicios fundamentales de Python. ¡Que disfrutes tu aventura de aprendizaje!