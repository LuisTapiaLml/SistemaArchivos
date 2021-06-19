import json
from helpers.getPath import getPath
from helpers.saveFileSystem import saveFileSystem
from helpers.getFileSystem import getFileSystem

def  crearDir( path ):
    
    _FILESYSTEM = getFileSystem()
    
    path = getPath( path , 'crearDir' )

    if not path :

        print(f"La ruta de subdirectorio o el archivo {path} no es valido ") 
        
        return False
        

    arbol = _FILESYSTEM

    exite = True

    for index ,  dir in enumerate( path ) :

        if dir in arbol :

            arbol = arbol[dir]

            if index == len( path ) -1 :                 
                exite = False

        else :

            arbol[dir] =  {}

            arbol = arbol[dir]
            


    if not exite :

        path = "/".join(path)
        
        print(f"Ya existe el subdirectorio o el archivo '{path}'")            

    saveFileSystem( _FILESYSTEM )
     









        

            
    




    




    

        



     



    
