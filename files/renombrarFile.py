

from dirs.renombrarDir import renombrarDir


def renomFile( comando ) :

    nombre_actual  = comando[0] 

    nuevo_nombre = comando[1] 

    if not ".txt" in   nombre_actual: 

        nombre_actual = nombre_actual + '.txt' 

    
    if not ".txt" in  nuevo_nombre: 

        nuevo_nombre = nuevo_nombre + '.txt' 


    if renombrarDir([nombre_actual , nuevo_nombre]) :

        print("Se renombro el archivo.")

        return True

    else: 
        print("Hubo un error")
        return False




    
