from os import path
from helpers.saveFileSystem import saveFileSystem
from helpers.getFileSystem import getFileSystem
from helpers.getGlobalData import getGlobalData
from helpers.getPath import getPath


def renombrarDir (comando) :
    
    _GLOBALDATA = getGlobalData()

    _FILESYSTEM = getFileSystem()

    path_actual =  getPath('','actual')

    arbol = _FILESYSTEM

    if not len( comando ) == 2 :

        print("La sintaxis del comando no es correcta") 

        return False
    
    nombre_actual =  getPath( comando[0] , "renomDir" )

    nombre_nuevo =  getPath( comando[1] , "renomDir" )

    if not len(nombre_actual)  ==  1 and not len(nombre_nuevo)  ==  1 :
        
        print("La sintaxis del comando no es correcta") 

        return False

    
    if len( path_actual ) == 0 :
    
        if not nombre_actual[0] in arbol : 
                    
            print("La carpeta que quiere renombrar no existe")

            return False

        arbol[nombre_nuevo[0]] = arbol.pop(nombre_actual[0])

    else:

        for index , dir in enumerate( path_actual ) :

            if dir in arbol:

                arbol = arbol[dir]

                if index  == len( path_actual ) - 1 : 
                    
                    if not nombre_actual[0] in arbol : 
                        
                        print("La carpeta que quiere renombrar no existe")

                        return False

                    arbol[nombre_nuevo[0]] = arbol.pop(nombre_actual[0])

                    return True

            else :

                print("hubo un error al procesar la informacion")
                return False


    saveFileSystem( _FILESYSTEM )

    # print("Ruta renombrada con éxito.")

    return True

    


    






    
    




    