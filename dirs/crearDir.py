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
    
    temp_arbol = {}

    contador = 0

    for index ,  dir in enumerate( path ) :

        temp_arbol =  filtrarArbol( dir , arbol )

        if len( temp_arbol ) :

            contador += 1

            arbol = temp_arbol[0]['hijos']

            continue
            
        else:

            arbol.append({
                "nombre" : dir,
                "tipo" : "carpeta" , 
                "hijos" : []
            })

            arbol = arbol[-1]["hijos"]


    if( contador == len( path )  ) :

        path = "/".join(path)
        
        print(f"Ya existe el subdirectorio o el archivo {path}")            

    saveFileSystem( _FILESYSTEM )
     


def filtrarArbol( dir , arbol ) :

    encontrado =  []    

    for carpeta in arbol : 

        if carpeta["nombre"] ==  dir :
            
            encontrado.append(carpeta)
                
    return encontrado

                








        

            
    




    




    

        



     



    
