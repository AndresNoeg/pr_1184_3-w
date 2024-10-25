print(" ")
print("Gomez Garcia Andres Noe 1184 3°w")
print(" ")
# Programa para sobrescribir un archivo
archivo = open("doc5.txt", "w")
archivo.write("He eliminado el contenido\n")
archivo.close()

# Abrir y leer el archivo después de sobrescribir
archivo = open("doc5.txt", "r")
print(archivo.read())
archivo.close()
