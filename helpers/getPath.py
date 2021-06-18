from helpers.getFileSystem import getFileSystem
from helpers.getGlobalData import getGlobalData

def getPath ( path = str , accion = str ) :
    
    _GLOBALDATA =  getGlobalData()
    
    path = path.split("/")

    if path[0] == '.' or path[0] == '' or path[0] == 'root' :  del path[0]
    
    if path[-1] == '' :  del path[-1]

    # if path[0] == 'root' and len (path ) > 1 : 
        
    #     del path[0]

    #     return path 

    PATHACTUAL =  _GLOBALDATA['__path'].split("/")

    if PATHACTUAL[0] == '' :
        del PATHACTUAL[0]


    if path[0] == ".." :
        
        for index , dir in enumerate( path ):

            if not dir == '..':
                return False

            if len( PATHACTUAL ) == 0 and not accion == 'navegarDir' :

                return False

            del PATHACTUAL[-1]

            del path[index]

    path = PATHACTUAL + path

    return path
        




