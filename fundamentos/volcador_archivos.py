import os

#He aqui un pequeño script para guardar el codigo de todos mis codigos de Python en un solo archivo de texto plano


#Mi directorio raiz
if os.getcwd() == '/storage/emulated/0':
	os.chdir('Scripts.py/')
	
	#Crear el archivo
	f = open('mis_codigos.txt', 'w')
	f.close()
	del f
	
	#Ahora si, abrimos y usamos un context manager
	with open('mis_codigos.txt', 'a') as f:
		f.write("Mis códigos de Python\n")
		archivos = os.listdir('./')[:91]
		
		for i, archivo in enumerate(archivos):
			cabecera = f'No.{i+1} {archivo[:-3].upper()}'
			f.write(cabecera)
			
			with open(archivo, 'r', encoding='utf-8') as codigo:
				#Saltos de linea para legibilidad
				f.write('\n\n')
				
				for linea in codigo:
					f.write(linea)
					
				f.write('\n\n')