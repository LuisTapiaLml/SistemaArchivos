

from helpers.saveFileSystem import saveFileSystem
import json
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath


def eliminarDir ( path ) :
    
    _FILESYSTEM = getFileSystem()
    
    _GLOBALDATA = getGlobalData()

    path = getPath( path )

    arbol = _FILESYSTEM

    if "/".join(path) == _GLOBALDATA['__path'] : 
        
        print("El directorio que intenta eliminar está en uso.")
        
        return False


    for index ,  dir in enumerate( path ) :

        if dir in arbol :

            if index == len( path ) -1 :      
                
                del arbol[dir]

            else :
                
                arbol = arbol[dir]
            
        else :

            print("El directorio que intenta eliminar no existe.",path)
        
            return False

    saveFileSystem( _FILESYSTEM )

    return True
     
     