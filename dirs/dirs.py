from dirs.moverDir import moverDir
from dirs.copiarDir import copiarDir
from dirs.renombrarDir import renombrarDir
from dirs.verContenido import verContenido
from dirs.eliminarDir import eliminarDir
from dirs.navegarDir import navegarDir
from dirs.crearDir import crearDir


def comandosDir(comando):
    
    modificador = comando[1]

    if modificador ==  'crear' :

        crearDir(comando[2])

    if modificador == 'ir' : 
        
        navegarDir( comando[2] )

    if modificador == 'eliminar' : 
        
        eliminarDir( comando[2] )

    if modificador == 'renom':

        renombrarDir( comando[2:] )

    if modificador ==  'copiar':

        copiarDir( comando[2:] ) 

    if modificador ==  'mover':

        moverDir( comando[2:] ) 
        

    if modificador == 'ver' :
        
        verContenido()
    
        


    