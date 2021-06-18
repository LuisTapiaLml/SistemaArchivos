

import json
import os


def saveGlobalData(globalData):
    
    filepath= '../data/config.json' 
    
    filepath = os.path.join(os.path.dirname(__file__), filepath)

    with open( filepath , 'w') as jsonfile:
            json.dump(globalData, jsonfile)
    
    return True
    

    
   