print(" ")
print("Gomez Garcia Andres Noe 1184 3°w")
print(" ")
# Programa para eliminar un archivo 
archivo = open("doc6.txt", "w")  # abrimos el archivo para el ejemplo
archivo.write("Este contenido ha sido eliminado.\n")
archivo.close()

archivo=open("doc6.txt", "r")
print(archivo.read())
archivo.close()
