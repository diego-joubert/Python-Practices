import os

ruta = input("Ruta de los archivos")
folder_path = ruta  # Cambia esto según tu ruta

# Recorre todos los archivos en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".lrc"):
        # Nuevo nombre cambiando .lrc por .txt
        new_name = filename.replace(".lrc", ".txt")
        
        # Renombra el archivo
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_name)
        
        os.rename(old_path, new_path)
        print(f"Renombrado: {filename} -> {new_name}")

print("¡Proceso completado!")