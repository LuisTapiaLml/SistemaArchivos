

import os
from helpers.getFileSystem import getFileSystem
from dirs.eliminarDir import eliminarDir
from helpers.getPath import getPath


def eliminarFile( comando  ) :

    _FILESYSTEM = getFileSystem()
    arbol = _FILESYSTEM
    
    id = ''
    
    exite = True

    carpeta= '../archivos/' 
    carpeta = os.path.join(os.path.dirname(__file__), carpeta)

    path  = getPath( comando )

    

    for index, dir in enumerate( path ):
        
        if  index == len( path ) -1 :
                if not ".txt" in dir :

                    dir += ".txt"


        if dir in arbol:     

            arbol = arbol[dir]

        else:
            
            exite = False
            break

    
    if not exite:

        print("El archivo que intenta eliminar no existe")

        return False

    else :

        id = arbol


    if eliminarDir(comando,"archivo"):

        if os.path.exists(f"{carpeta}/{id}"):

            os.remove(f"{carpeta}/{id}")

            print("Archivo borrado.")
        
        else:
            print("El archivo fisico no existe")

            return False


        

        

