#La versión de Python (Python 3.8.16) con una ruta al archivo ejecutable, si es posible
#La codificación del archivo (normalmente, coding: utf-8)

preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"


# Almacenar el valor de cada subsecuencia
lsInsulin = "malwmrllpllallalwgpdpaaa"
bInsulin = 	"fvnqhlcgshlvealylvcgergffytpkt"
aInsulin = 	"giveqcctsicslyqlenycn"
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"


# Suma el valor de las subsecuencias más pequeñas
insulin = bInsulin + aInsulin


# Imprimiendo la secuencia de insulina humana
print("La secuencia de la insulia humana 🙉 : ", preproInsulin)

# Imprimiendo los valores usando concatenación
print("El valor de la cadena aInsulin 🐒: " + aInsulin)

# Calcular el peso de los aminociados en la insulina

# Define el valor del peso de cada aminoacido
aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19} 

# Conteo de cuantas veces aparece cada aminoacido en la cadena   
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in ['A', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']}) 

###Equivalente a:
aaCountInsulin = {}

aminoacidos =['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']

for x in aminoacidos:
    #Buscar cuantas veces aparece el aminoacido en la cadana
    #Es necesario el upper para que coincida con las mayusculas
    conteo= insulin.upper().count(x)
    
    #Guardar el valor en el diccionario 
    aaCountInsulin[x] = float(conteo)
    ###Guarda el valor en formato flotante
    print("Diccionario" , aaCountInsulin)
    
# Multiplicar el contador por el peso(masa)
pesos_totales = {}

for x in ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']:
    valor = aaCountInsulin[x] * aaWeights[x]
    
    #Guardar en el diccionario
    pesos_totales[x]= valor 
    
    print("El peso molecular aproximado de la insulina: ", pesos_totales)