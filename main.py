from helpers.getGlobalData import getGlobalData
import os
from helpers.getPath import getPath
from dirs.dirs import comandosDir



def espera_comando():
    
    _GLOBALDATA = getGlobalData()

    comando = " ".join(input(f"root/{_GLOBALDATA['__path']}:>").split()).split(" ")

    if comando[0] ==  "dir" :

        comandosDir(comando)

    if( comando[0] == "cls"):

        os.system('cls')


    espera_comando()





espera_comando()

