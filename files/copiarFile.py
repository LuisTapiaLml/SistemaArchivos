

from dirs.moverDir import moverDir
from helpers.getPath import getPath


def copiarFile(comando):

    if not len( comando ) == 2 :

        print("Error de sintaxis")

        return False  


    path_actual = getPath( comando[0] )

    path_nuevo =  getPath( comando[1] )

    if not ".txt" in path_actual[-1] :

        path_actual[-1] =  path_actual[-1] + '.txt'

    
    if moverDir( [ "root:/"+  ("/").join(path_actual) , "root:/"+  ("/").join(path_nuevo) ] , 'copiarFile' ):

        print("Se copió con éxito")

    else : 

        print("no se pudo copiar el archivo")