
import os
import shutil
import pathlib


Ruta = input("Específica la donde se en cuentran los archivos que quieres borrar: ")
texto = input("Proporciona algúna palabra que contenga el archivo que quieras borrar: ")

print(f"La ruta seleccionada es: {Ruta} y la palabra de los archivos es: {texto}")

confirm = input("si la ruta y la palabra clave son correctas escribe y, si es incorrecto n: \n")

# EL USUARIO CONFIRMA QUE LAS RUTAS SON LAS CORRECTAS
if confirm.lower() == "y":
    print("[*] Confirmado")
else:
    print("[-] Abortado")
    exit()

#COMPROBAMOS QUE LA RUTA PROPORCIONADA EXISTA

if os.path.exists(Ruta):
    print(f"[*] La ruta {Ruta} existe")
else:
    print(f"[-] La ruta {Ruta} no existe, cerrando script")
    exit()


archivos = os.listdir(ruta)
for archivo in archivos:
    print(archivo)