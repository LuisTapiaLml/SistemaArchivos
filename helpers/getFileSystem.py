import json
import os


def getFileSystem():
    
    filepath= '../data/fileSystem.json' 
    
    filepath = os.path.join(os.path.dirname(__file__), filepath)

    f =  open(filepath,"r")

    data = json.loads(  f.read() ) 

    f.close()

    return data 
