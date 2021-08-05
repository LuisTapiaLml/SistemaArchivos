import os


def comandos(  ) : 

    filepath= '../data/fileSystem.json' 
    
    filepath = os.path.join(os.path.dirname(__file__), filepath)
    
    data = {
        'concurrencia' : os.path.join(os.path.dirname(__file__), 'scripts/concurrencia/bernstein.py' ),
        'buffering' : os.path.join(os.path.dirname(__file__), 'scripts/buffering&Spooling.py' ),
        'cache' : os.path.join(os.path.dirname(__file__), 'scripts/cache.py' ),
        'interrupciones' : os.path.join(os.path.dirname(__file__), 'scripts/interrupciones.py' ),
    }

    return data