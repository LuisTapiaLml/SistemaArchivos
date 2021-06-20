

from helpers.saveFileSystem import saveFileSystem
import json
from helpers.getPath import getPath
from helpers.getFileSystem import getFileSystem
from helpers.getGlobalData import getGlobalData


def copiarDir(comando):

    _FILESYSTEM = getFileSystem() 
    
    ruta_original = getPath( comando[0] )

    ruta_copia = getPath( comando[1] )

    arbol = _FILESYSTEM
    nuevo_arbol = _FILESYSTEM

    carpeta = {}

    for index , dir in enumerate( ruta_original ):    

        if dir in arbol:

            arbol = arbol[dir]

            if index == len( ruta_original ) - 1 :
                
                carpeta = arbol

        else:
            
            print("La carpeta que quiere copiar no existe")
            
            return False

    if len ( ruta_copia ) == 0 :
        
        nuevo_arbol[ruta_original[-1]] =  carpeta

    else:    

        for index , dir in enumerate( ruta_copia ):
        
            if dir in nuevo_arbol:

                nuevo_arbol = nuevo_arbol[dir]

                if index == len( ruta_copia ) - 1 :

                    nuevo_arbol[ruta_original[-1]] =  carpeta

            else:
                
                print("La carpeta que quiere copiar no existe")
                
                return False 

    # print("Ruta copiada con éxito.")

    saveFileSystem(_FILESYSTEM)

    return True

    