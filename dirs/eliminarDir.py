

from helpers.saveFileSystem import saveFileSystem
import json
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath


def eliminarDir ( path , accion = '' ) :
    
    _FILESYSTEM = getFileSystem()
    
    _GLOBALDATA = getGlobalData()

    path = getPath( path )

    arbol = _FILESYSTEM

    if "/".join(path) == _GLOBALDATA['__path'] : 
        
        print("El directorio que intenta eliminar está en uso.")
        
        return False


    for index ,  dir in enumerate( path ) :

        if  index == len( path ) -1  and accion == "archivo" :
                
                if not ".txt" in dir :

                    dir += ".txt"

        if dir in arbol :

            if index == len( path ) -1 :      
                
                del arbol[dir]

            else :
                
                arbol = arbol[dir]
            
        else :

            print("El directorio que intenta eliminar no existe.",dir)
        
            return False

    # if accion == '' :

    #     print("Ruta eliminada con éxito.")

    saveFileSystem( _FILESYSTEM )

    return True
     
     