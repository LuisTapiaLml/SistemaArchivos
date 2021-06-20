

from files.crearFile import crearFile


def comandosFile(comando) : 

    modificador = comando[1]

    if modificador == 'crear' : 

        crearFile( comando[2:] )

        