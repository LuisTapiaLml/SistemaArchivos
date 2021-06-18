

import json
from helpers.saveGlobalData import saveGlobalData
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath


def navegarDir ( path ) : 

    _FILESYSTEM = getFileSystem()
    
    _GLOBALDATA = getGlobalData()

    path = getPath( path , 'navegarDir' )

    temp_path  = path[:]

    for dir in temp_path : 

        respuesta = buscarCarpeta (dir , _FILESYSTEM) 

        if not respuesta['estado'] : 
            
            print(f"La ruta de subdirectorio o el archivo {path} no es valido ") 

            return False
        
        else:

            _FILESYSTEM =  respuesta['data']


    
    _GLOBALDATA['__path'] = "/".join( path ) 

    saveGlobalData( _GLOBALDATA )

    return True

        

def buscarCarpeta (dir , _FILESYSTEM) :

    respuesta = {
        'estado' : False ,
        'data' : []
    }

    for carpeta in _FILESYSTEM :

        if ( carpeta['nombre'] ==  dir ) :
            
            respuesta = {
                'estado' : True ,
                'data' : carpeta['hijos']
            }
        

    return respuesta
    
        
    
