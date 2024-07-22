def save_sequence(filename, sequence):
    # Esta función guarda una secuencia en un archivo
    with open(filename, 'w') as file:
        file.write(sequence)

# Paso 1: Leer el archivo con la secuencia completa
with open('preproinsulin-seq.txt', 'r') as file:
    full_sequence = file.read().strip()

# Paso 2: Dividir la secuencia en subsecuencias
l_sequence = full_sequence[:24]  # Aminoácidos 1-24
b_sequence = full_sequence[24:54]  # Aminoácidos 25-54
c_sequence = full_sequence[54:89]  # Aminoácidos 55-89
a_sequence = full_sequence[89:110]  # Aminoácidos 90-110

# Paso 3: Escribir cada subsecuencia en un archivo diferente
save_sequence('lsinsulin-seq-clean.txt', l_sequence)
save_sequence('binsulin-seq-clean.txt', b_sequence)
save_sequence('cinsulin-seq-clean.txt', c_sequence)
save_sequence('ainsulin-seq-clean.txt', a_sequence)