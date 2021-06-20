

from io import StringIO
import os
import uuid
from dirs.eliminarDir import eliminarDir
from helpers.saveFileSystem import saveFileSystem
import json
from helpers.getPath import getPath
from helpers.getFileSystem import getFileSystem


def moverDir(comando , accion='' ):

    _FILESYSTEM = getFileSystem() 
    
    ruta_original = getPath( comando[0] )

    ruta_copia = getPath( comando[1] )

    arbol = _FILESYSTEM
    nuevo_arbol = _FILESYSTEM
    copia= _FILESYSTEM

    ids = {
        "viejo_id" : '' ,
        "nuevo_id" : str( uuid.uuid4() )
    }

    carpeta = {}
 

    for index , dir in enumerate( ruta_original ):    

        if dir in arbol:

            arbol = arbol[dir]

            if index == len( ruta_original ) - 1 :
                
                if accion == 'copiarFile':

                    ids["viejo_id"] = arbol

                    carpeta = ids["nuevo_id"]
                
                else:    

                    carpeta = arbol

                del arbol

        else:
            
            print("La carpeta que quiere mover no existe 1")
            
            return False

    for index , dir in enumerate( ruta_copia ):
       
        if dir in nuevo_arbol:

            nuevo_arbol = nuevo_arbol[dir]

            if index == len( ruta_copia ) - 1 :

                nuevo_arbol[ruta_original[-1]] =  carpeta

        else:
            
            print("La carpeta que quiere mover no existe 2")
            
            return False 
    
    saveFileSystem(_FILESYSTEM)



    if accion == 'copiarFile':

       copiarArchivo( ids ) 
    
    else:
        
        eliminarDir(comando[0]) 

    return True

    
def copiarArchivo( ids ):
    
    carpeta= '../archivos/' 
    
    carpeta = os.path.join(os.path.dirname(__file__), carpeta)

    viejo_archivo =  open( carpeta + f"/{ ids['viejo_id'] }" , "r" )

    nuevo_archivo = open( carpeta + f"/{ ids['nuevo_id'] }" , "w" )

    nuevo_archivo.write( viejo_archivo.read() )

    viejo_archivo.close()

    nuevo_archivo.close()