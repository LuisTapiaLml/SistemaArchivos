#Solución de un sistema de ecuaciones de segundo orden
import math
variable10  = float( input ( ) )
variable9 = float( input ( ) )
variable8 = float(input ( ) )
variable7 = 0
variable6 = 0
variable5 = 4 * variable10 * variable8
variable4 = variable9 * variable9
variable3 = math.sqrt( variable4 - variable5 )
variable1 = 2 * variable10
variable11 = variable9 * -1
if variable10 == 0 :
    print ( "Division entre 0, es indetermiando" )
else:
    if variable5 > variable4 :
        print ( "Raíz cuadrada de números complejos" )
    else:
        variable7 = ( ( variable11 + variable3 ) / variable1 )
        variable6 = ( ( variable11 -  variable3 ) / variable1 )
        print("primer raíz = {:.5}".format ( variable7 ) )
        print("segunda raiz = {:.5}".format ( variable6 ) )
    
    
    


