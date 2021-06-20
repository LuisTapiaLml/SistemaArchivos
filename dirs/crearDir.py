import json
from helpers.getPath import getPath
from helpers.saveFileSystem import saveFileSystem
from helpers.getFileSystem import getFileSystem

def  crearDir( path , nombreArchivo = ''  ):
    
    _FILESYSTEM = getFileSystem()
    
    path = getPath( path , 'crearDir' )

    if not path :

        print(f"La ruta de subdirectorio o el archivo {path} no es valido ") 
        
        return False
        

    arbol = _FILESYSTEM

    existe = True

    for index ,  dir in enumerate( path ) :

        if dir in arbol :

            arbol = arbol[dir]

            if index == len( path ) -1 :                 
                existe = False

        else :

            if index == len( path ) -1 and not nombreArchivo == '' :
                
                arbol[dir] = nombreArchivo

                # arbol = arbol[dir]

                break

            arbol[dir] =  {}

            arbol = arbol[dir]
            

    if not existe :

        path = "/".join(path)
        
        print(f"Ya existe el subdirectorio o el archivo '{path}'")            


    # if nombreArchivo == '' :
        # print("Ruta creada con éxito.")

    saveFileSystem( _FILESYSTEM )
     
    return True








        

            
    




    




    

        



     



    
