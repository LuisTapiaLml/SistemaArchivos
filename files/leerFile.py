

from helpers.getFileSystem import getFileSystem
from helpers.getPath import getPath
import os


def leerFile ( comando ) :

    _FILESYSTEM =getFileSystem()

    arbol = _FILESYSTEM

    carpeta= '../archivos/' 
    
    carpeta = os.path.join(os.path.dirname(__file__), carpeta)

    path = getPath( comando )

    if not ".txt" in path[-1]  :
        path[-1] = path[-1] + '.txt'


    for index , dir in enumerate( path ):

        if dir in arbol :

            arbol = arbol[dir]

        else:
            print("No archivo que intenta leer no existe")

            return False

    carpeta += f'/{arbol}'


    f = open( carpeta , "r" )

    print( f.read() ) 
    
        