

import json
import os


def saveFileSystem(fileSistem):
    
    filepath= '../data/fileSystem.json' 
    
    filepath = os.path.join(os.path.dirname(__file__), filepath)

    with open( filepath , 'w') as jsonfile:
            json.dump(fileSistem, jsonfile)
    

    
   