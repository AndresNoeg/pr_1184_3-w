print(" ")
print("Gomez Garcia Andres Noe 1184 3°w")
print(" ")
# Programa para anexar contenido a un archivo existente
archivo = open("doc4.txt", "a")
archivo.write("Now the file has more content!\n")
archivo.close()

# Abrir y leer el archivo después de añadir
archivo = open("doc4.txt", "r")
print(archivo.read())
archivo.close()
