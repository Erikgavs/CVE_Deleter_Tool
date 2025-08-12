
import os
import shutil
import pathlib


Ruta = input("\nEspecífica la donde se en cuentran los archivos que quieres borrar:")
texto = input("\nProporciona algúna palabra que contenga el archivo que quieras borrar: ")

print(f"La ruta seleccionada es: {Ruta} y la palabra de los archivos es: {texto}")

confirm = input("si la ruta y la palabra clave son correctas escribe y, si es incorrecto n: \n")

# EL USUARIO CONFIRMA QUE LAS RUTAS SON LAS CORRECTAS
if confirm.lower() == "y":
    print("[*] Confirmado")
elif confirm.lower() == "n":
    print("[-] Abortado")
    exit()
else:
    exit()

#COMPROBAMOS QUE LA RUTA PROPORCIONADA EXISTA

if os.path.exists(Ruta):
    print(f"[*] La ruta {Ruta} existe")
else:
    print(f"[-] La ruta {Ruta} no existe, cerrando script")
    exit()


archivos = os.listdir(Ruta)

for archivo in archivos:
    if texto in archivo:
        print(f"[*] Archivo encontrado: {archivo}")

        # BORRADO DEL ARCHIVO
        ruta_completa = os.path.join(Ruta, archivo)
        os.rmdir(ruta_completa)
