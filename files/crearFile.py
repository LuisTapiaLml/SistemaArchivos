

from dirs.crearDir import crearDir
import os
from helpers.getPath import getPath
from os import path
import uuid

def crearFile ( comando ) :

    if len( comando ) > 2 :

        print("La sintaxis del comando no es correcta") 

        return False
    
    nombre_archivo = ''
    path_file =  getPath( comando[0] )

    carpeta= '../archivos/' 
    
    carpeta = os.path.join(os.path.dirname(__file__), carpeta)

    id = str ( uuid.uuid4() )

    if not len( comando ) == 2 :
        comando.append("")

    if not ".txt"  in  comando[0]:
        
        comando[0] = comando[0] + '.txt'

    carpeta = carpeta + f"/{id}.txt"

    nuevo_archivo = open(carpeta,"w+") 

    nuevo_archivo.write( comando[1] )

    nuevo_archivo.close()

    if crearDir( comando[0] , f"{id}.txt" ) : 
        print("Archivo creado con éxito.")   


    











    
