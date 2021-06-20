

from helpers.getPath import getPath
from os import path


def crearFile ( comando ) :

    print( comando )

    if len( comando ) > 2 :

        print("La sintaxis del comando no es correcta") 

        return False    
    
    
    path_file =  getPath( comando[0] )

    "contenido"





    
