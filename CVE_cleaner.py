
import os
import shutil


Ruta = input("\nEspecífica la ruta donde se en cuentran los archivos que quieres borrar: ")
texto = input("\nProporciona algúna palabra que contenga el archivo que quieras borrar: ")

print(f"\nLa ruta seleccionada es: {Ruta} \n la palabra de los archivos es: {texto}")

confirm = input("\nsi la ruta y la palabra clave son correctas escribe y\, si es incorrecto n\: \n\n")

# EL USUARIO CONFIRMA QUE LAS RUTAS SON LAS CORRECTAS
if confirm.lower() == "y":
    print("\n[*] Confirmado")
elif confirm.lower() == "n":
    print("\n[-] Abortado")
    exit()
else:
    exit()

#COMPROBAMOS QUE LA RUTA PROPORCIONADA EXISTA

if os.path.exists(Ruta):
    print(f"\n[*] La ruta {Ruta} existe")
else:
    print(f"\n[-] La ruta {Ruta} no existe, cerrando script")
    exit()


archivos = os.listdir(Ruta)

for archivo in archivos:
    if texto in archivo:
        print("\n[*] Archivo o carpeta encontrada")

        # BORRADO DEL ARCHIVO
        ruta_completa = os.path.join(Ruta, archivo)
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)
            print(f"\nArchivo eliminado correctamente: {archivo}\n")
        elif os.path.isdir(ruta_completa):
            shutil.rmtree(ruta_completa) # BORRA CARPETA Y Su contenido
            print(f"\nCarpeta eliminada correctamente: {archivo} \n")
        else:
            print("\n[-] Error al borrar los directorios o archivos")
