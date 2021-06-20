

from files.copiarFile import copiarFile
from files.modificarFile import modificarFile
from files.leerFile import leerFile
from files.moverFile import moverFile
from files.renombrarFile import renomFile
from files.eliminarFile import eliminarFile
from files.crearFile import crearFile


def comandosFile(comando) : 

    modificador = comando[1]

    if modificador == 'crear' : 

        crearFile( comando[2:] )
    
    if modificador == 'eliminar' : 

        eliminarFile( comando[2] )

    
    if modificador == 'renom':

        renomFile(comando[2:] )


    if modificador == 'mover' :

        moverFile( comando[2:] ) 

    
    if modificador == 'leer' :

        leerFile( comando[2] ) 

    if modificador == 'mod' :

        modificarFile( comando[2:] ) 

    if modificador == 'copiar':

        copiarFile( comando[2:] )
        