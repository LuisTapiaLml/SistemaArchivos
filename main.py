from dirs.verArbol import verArbol
from helpers.getGlobalData import getGlobalData
import os
from dirs.dirs import comandosDir



def espera_comando():
    
    _GLOBALDATA = getGlobalData()

    comando = " ".join(input(f"\nroot:/{_GLOBALDATA['__path']}>").split()).split(" ")

    if comando[0] ==  "dir" :

        comandosDir(comando)

    if comando[0] == "cls":

        os.system('cls')

    if comando[0] == "tree" : 

        verArbol()



    espera_comando()



espera_comando()

