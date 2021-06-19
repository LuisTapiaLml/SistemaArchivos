

from helpers.getPath import getPath
from os import path
from helpers.getGlobalData import getGlobalData
from helpers.getFileSystem import getFileSystem


def verArbol() :
    
    _FYLESYSTEM = getFileSystem()
    _GLOBALDATA = getGlobalData()

    path =  getPath( _GLOBALDATA['__path'] , "tree" )

    arbol = ''

    for dir in path :
        
        if dir in _FYLESYSTEM :

            _FYLESYSTEM = _FYLESYSTEM[dir]

        else:

            print(path)

            print("Hubo un error al procesar el comando")

            return False   

    # keys = _FYLESYSTEM.keys()

    # for key in keys :

    #     arbol += f"{key} \n" 
    print("\n")

    formatoArbol( _FYLESYSTEM , 0)

    print( arbol )

    return True



def formatoArbol(directorio,s):
    
    linea = ""

    if not isinstance(directorio,dict) and not isinstance(directorio,list):
        if s > 0 : linea = "└"
        print("   "*s+linea+"-"*s+str(directorio) )
    else:
        for key in directorio:
            if s > 0 : linea = "└"
            print("   "*s+linea+"-"*s+str( key ) ) 
            if not isinstance(directorio,list):
                formatoArbol(directorio[key],s+1)