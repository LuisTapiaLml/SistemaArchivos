

from helpers.getPath import getPath
from os import path
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem


def verContenido() :
    
    _FYLESYSTEM = getFileSystem()
    _GLOBALDATA = getGlobalData()

    path =  getPath('','actual')

    arbol = ''
    
    for dir in path :
        
        if dir in _FYLESYSTEM :

            _FYLESYSTEM = _FYLESYSTEM[dir]

        else:

            print("Hubo un error al procesar el comando")

            return False   

    keys = _FYLESYSTEM.keys()

    for key in keys :

        arbol += f"{key} \n" 

    print( arbol )

    return True
