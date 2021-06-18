

import json
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath


def eliminarDir ( path ) :
    
    _FILESYSTEM = getFileSystem()
    
    _GLOBALDATA = getGlobalData()

    path = getPath( path )

    temp_file_system = _FILESYSTEM

    if "/".join(path) == _GLOBALDATA['__path'] : 
        
        print("El directorio que intenta eliminar está en uso.")
        
        return False

    
    for index , dir in enumerate( path )  : 

        respuesta = buscarCarpeta (dir , temp_file_system) 

        if not respuesta['estado'] : 
            
            print(f"La ruta de subdirectorio o el archivo {path} no es valido ") 

            return False
        
        else:

            if ( index == len( path ) - 1 and respuesta['estado']  ):

                print('se supone que se elimino')

                del respuesta['carpeta']
                
                print( json.dumps( respuesta , indent= 4  ))

            else:

                temp_file_system =  respuesta['data']


    print(json.dumps( _FILESYSTEM , indent= 4  ))
                



def buscarCarpeta (dir , _FILESYSTEM) :

    respuesta = {
        'estado' : False ,
        'data' : [],
        "carpeta" : {}
    }

    for carpeta in _FILESYSTEM :

        if ( carpeta['nombre'] ==  dir ) :
            
            respuesta = {
                'estado' : True ,
                'data' : carpeta['hijos'],
                "carpeta" : carpeta
            }
        

    return respuesta