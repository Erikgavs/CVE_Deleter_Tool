
import os
import shutil

print(r"""
  ||||||||    ||         ||||||||||         ||          ||||     ||    ||||||||||     ||||||||
||            ||         ||               ||  ||        || ||    ||    ||             ||     ||
||            ||         ||              ||    ||       ||  ||   ||    ||             ||    ||  
||            ||         |||||          ||||||||||      ||   ||  ||    |||||          ||   || 
||            ||         ||            ||        ||     ||    || ||    ||             ||    ||
  ||||||||    ||||||||   ||||||||||   ||          ||    ||      |||    ||||||||||     ||     || 
      
[*] Script developed by Erik Gavilán
[*] Be careful when using this script, may delete important files if used incorrectly
[*] For ethical purposes only
""")


reset = "\033[0m"
azul = "\033[34m"
rojo = "\033[31m"
verde = "\033[32m"

Ruta = input("\nEspecífica la ruta donde se en cuentran los archivos que quieres borrar: ")
texto = input("\nProporciona algúna palabra que contenga el archivo que quieras borrar: ")

print(f"\nLa ruta seleccionada es: {azul}{Ruta}{reset} \n\nLa palabra de los archivos es: {azul}{texto}{reset}")

confirm = input(f"\nSi la ruta y palabra clave son correctas escribe {azul}S{reset}, si es incorrecto {azul}N{reset}: \n\n")

# Si la ruta y palabra clave son correctas escribe S, si es incorrecto N

# EL USUARIO CONFIRMA QUE LAS RUTAS SON LAS CORRECTAS
if confirm.upper() == "S":
    print(f"\n{verde}[*] Confirmado{reset}")
elif confirm.upper() == "N":
    print(f"\n{rojo}[-] Abortado{reset}")
    exit()
else:
    exit()

#COMPROBAMOS QUE LA RUTA PROPORCIONADA EXISTA

if os.path.exists(Ruta):
    print(f"\n{verde}[*]{reset} La ruta {azul}{Ruta}{reset} existe")
else:
    print(f"\n{rojo}[-]{reset} La ruta {azul}{Ruta}{reset} no existe, cerrando script")
    exit()


archivos = os.listdir(Ruta)
verificar = False

for archivo in archivos:
    if texto in archivo:
        print(f"\n{verde}[*]{reset} Archivo o carpeta encontrada")

        # BORRADO DEL ARCHIVO
        ruta_completa = os.path.join(Ruta, archivo)
        if os.path.isfile(ruta_completa):
            os.remove(ruta_completa)
            print(f"\n{verde}[*]{reset} Archivo eliminado correctamente: {azul}{archivo}{reset}\n")
            verificar = True
        elif os.path.isdir(ruta_completa):
            shutil.rmtree(ruta_completa) # BORRA CARPETA Y Su contenido
            print(f"\n{verde}[*]{reset} Carpeta eliminada correctamente: {azul}{archivo}{reset} \n")
            verificar = True
        else:
            print(f"\n{rojo}[-] Error al borrar los directorios o archivos{reset}")

if not verificar:
    print("[-] Archivo no encontrado")
    exit()
