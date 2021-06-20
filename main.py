import os
import shlex

from dirs.dirs import comandosDir
from files.files import comandosFile
from dirs.verArbol import verArbol
from helpers.getGlobalData import getGlobalData


def espera_comando():
    
    _GLOBALDATA = getGlobalData()

    comando = " ".join(input(f"\nroot:/{_GLOBALDATA['__path']}>").split())

    comando =  shlex.split( comando )

    if comando[0] == "cls":

        os.system('cls')

    elif comando[0] == "tree" : 

        verArbol()

    elif len( comando ) < 2 :
        
        espera_comando()
        
        return False
        

    if comando[0] ==  "dir" :

        comandosDir(comando)

    elif comando[0] ==  "file" :

        comandosFile(comando)
        

    espera_comando()



espera_comando()

