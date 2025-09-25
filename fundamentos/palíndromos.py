ruta = input("Escriba la ruta del archivo a leer: ")
archivo = open(ruta, 'r')
texto = archivo.read()
  
contar = 0
  
for palabra in texto.split(' '):
  if palabra == palabra[::-1]:
    contar += 1
  
if not contar:
  print ("No hay palabras palíndromas en el archivo")
else:
  print ("Palabras palíndromas encontradas: ", contar)
  
archivo.close()