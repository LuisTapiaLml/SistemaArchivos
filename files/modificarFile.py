

import os
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath
from os import path


def modificarFile( comando ):

    if not len(comando) == 2 :
       print("Error de sintaxis")
       return False

    _FILESYSTEM =getFileSystem()

    arbol = _FILESYSTEM

    carpeta= '../archivos/' 
    
    carpeta = os.path.join(os.path.dirname(__file__), carpeta)

    path = getPath( comando[0] )

    if not ".txt" in path[-1]  :
        path[-1] = path[-1] + '.txt'

    
    for index , dir in enumerate( path ):

        if dir in arbol :

            arbol = arbol[dir]

        else:
            print("No archivo que intenta leer no existe")

            return False

    carpeta += f'/{arbol}'


    nuevo_archivo = open(carpeta,"w+") 

    nuevo_archivo.write( comando[1] )

    nuevo_archivo.close()

    print("Se modificó con éxito.")
