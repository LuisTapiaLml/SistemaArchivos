

from dirs.eliminarDir import eliminarDir
from helpers.saveFileSystem import saveFileSystem
import json
from helpers.getPath import getPath
from helpers.getFileSystem import getFileSystem


def moverDir(comando):

    _FILESYSTEM = getFileSystem() 
    
    ruta_original = getPath( comando[0] )

    ruta_copia = getPath( comando[1] )

    arbol = _FILESYSTEM
    nuevo_arbol = _FILESYSTEM
    copia= _FILESYSTEM

    carpeta = {}

    for index , dir in enumerate( ruta_original ):    

        if dir in arbol:

            arbol = arbol[dir]

            if index == len( ruta_original ) - 1 :
                
                carpeta = arbol

                del arbol

        else:
            
            print("La carpeta que quiere mover no existe")
            
            return False


    for index , dir in enumerate( ruta_copia ):
       
        if dir in nuevo_arbol:

            nuevo_arbol = nuevo_arbol[dir]

            if index == len( ruta_copia ) - 1 :

                nuevo_arbol[ruta_original[-1]] =  carpeta

        else:
            
            print("La carpeta que quiere mover no existe")
            
            return False 

    
    # print( json.dumps( _FILESYSTEM , indent=4 ) )
    
    saveFileSystem(_FILESYSTEM)

    eliminarDir(comando[0])

    return True



    