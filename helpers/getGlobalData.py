import os,json

def getGlobalData():
    
    filepath= '../data/config.json' 
    
    filepath = os.path.join(os.path.dirname(__file__), filepath)

    f =  open(filepath,"r")
    
    data =  json.loads(f.read())
    
    f.close()

    return data 

