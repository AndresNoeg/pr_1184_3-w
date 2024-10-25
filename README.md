# pr_1184_3-w

print(" ")

print("Gomez Garcia Andres Noe 1184 3°w")

print(" ")
# Programa para leer un archivo

archivo = open("doc1.txt", "r")

print(archivo.read())

archivo.close()

![image](https://github.com/user-attachments/assets/e00bc5ad-617c-4178-b8e3-ad2f9594b971)

print(" ")
print("Gomez Garcia Andres Noe 1184 3°w")
print(" ")
# Programa para abrir un archivo en una ubicación diferente
archivo = open("doc2.txt", "r")
print(archivo.read())
archivo.close()

![image](https://github.com/user-attachments/assets/fbb1f2ec-d9c1-490f-b634-5b7c20d795d2)

print(" ")
print("Gomez Garcia Andres Noe 1184 3°w")
print(" ")
# Programa para leer los primeros 5 caracteres de un archivo
archivo = open("doc3.txt", "r")
print(archivo.read(5))
archivo.close()

![image](https://github.com/user-attachments/assets/ba040b23-e728-48c1-9244-20b34b029a96)

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

![image](https://github.com/user-attachments/assets/ebd9bbbc-b37b-4307-9bea-10255a3c4eef)

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

![image](https://github.com/user-attachments/assets/f0a73c28-650a-4ebe-99dd-8f140c3a32f3)







