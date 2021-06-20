

import json
from helpers.saveGlobalData import saveGlobalData
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath


def navegarDir ( path ) : 

    _FILESYSTEM = getFileSystem()
    
    _GLOBALDATA = getGlobalData()

    path = getPath( path , 'navegarDir' )


    for index ,  dir in enumerate( path ) :

        if dir in _FILESYSTEM :

            _FILESYSTEM = _FILESYSTEM[dir]

            _FILESYSTEM

        else:
            
            print(f"La ruta de subdirectorio o el archivo {path} no es valido ") 
            
            return False


    _GLOBALDATA['__path'] = "/".join( path ) 

    saveGlobalData( _GLOBALDATA )

    return True

        
    
        
    
