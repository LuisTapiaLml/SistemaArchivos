from dirs.eliminarDir import eliminarDir
from dirs.navegarDir import navegarDir
from dirs.crearDir import crearDir


def comandosDir(comando):
    
    modificador = comando[1]

    if modificador ==  'crear' :

        crearDir(comando[2])

    if modificador == 'go' : 
        
        navegarDir( comando[2] )

    if modificador == 'eliminar' : 
        
        eliminarDir( comando[2] )
    
        


    