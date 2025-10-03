# Crear y escribir en el archivo my_notes.txt
file = open("my_notes.txt", "w")  # Abrimos el archivo en modo escritura 'w'
file.write("Nota 1: Recordar correr todos los días.\n")
file.write("Nota 2: Comprar frutas y verduras para la semana.\n")
file.write("Nota 3: Recordar fecha de cumpleaños de mi amiga.\n")
file.close()  # Cerramos el archivo después de escribir

# Leer el contenido del archivo línea por línea
file = open("my_notes.txt", "r")  # Abrimos el archivo en modo lectura 'r'

line = file.readline()  # Leemos la primera línea
while line:              # Mientras exista contenido en la línea
    print(line.strip())  # Mostramos la línea en consola (sin salto extra)
    line = file.readline()  # Leemos la siguiente línea

file.close()  # Cerramos el archivo después de leer
