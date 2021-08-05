import json
from math import log
import os 

dir_codigo_1 =  os.path.join(os.path.dirname(__file__), 'comandos/scripts/concurrencia/codigo1.py')

dir_codigo_2 =  os.path.join(os.path.dirname(__file__), 'comandos/scripts/concurrencia/codigo2.py')

codigo2 = open(dir_codigo_2,'r')
codigo1 = open(dir_codigo_1,'r')

operadoresLectura = ['==' , '%' , "<" , ">" , ")" , "(" , "+" , "-" ,"*" ,"/" ]

operadoresEscritura = ['=' , '%' , "+=" , '-='  ]

def validarLineas ( lineas ) :
    
    lineasValidadas = {}

    for indexLinea ,  linea in enumerate( lineas ) :

        partesLinea = linea.split(" ")

        lineasValidadas['linea' + str(indexLinea) ] = {
            "escritura" : [ ] ,
            "lectura" : [ ]
        }

        for indexParte ,  parteLinea in enumerate(partesLinea) : 

            if 'variable' in  parteLinea : 

                operadorDerecha = ''
                operadorIzquierda =  ''

                if indexParte + 1 <= len(partesLinea) -1 :
                    
                    operadorDerecha = partesLinea[ indexParte + 1 ] 
                else: 
                    operadorDerecha = 0

                if indexParte - 1 >= 0 :
                    operadorIzquierda = partesLinea[ indexParte - 1 ]
                else:
                    operadorIzquierda = 0 

                # print( indexParte , len(partesLinea) , partesLinea  , operadorDerecha , operadorIzquierda)

                if operadorDerecha in operadoresEscritura :

                    lineasValidadas['linea' + str(indexLinea) ]['escritura'].append( parteLinea  )

                elif operadorDerecha in operadoresLectura or operadorIzquierda in operadoresLectura:
                    
                    lineasValidadas['linea' + str(indexLinea) ]['lectura'].append( parteLinea  )
                
                elif operadorIzquierda == '=' : 

                    lineasValidadas['linea' + str(indexLinea) ]['lectura'].append( parteLinea  )

                # print('operadores' , operadorIzquierda , operadorDerecha)

                

    return lineasValidadas 


def limpiarLineas( file ) :

    lineas = [] 
    for x in file :

        if not x == '' :
            
            x = " ".join(x.replace("\n","").strip().split())

            if not x == '' :

                lineas.append( x )

    
    
    return validarLineas( lineas )



base1 = limpiarLineas( codigo1 ) 
base2 = limpiarLineas( codigo2 ) 

def compararCodigos ( cod1 , cod2 ) : 

    longitud = 0 

    contador = 0 

    if len( cod1 ) < len ( cod2 )  : 
        longitud = len( cod1 )
    else:
        longitud = len( cod2 )

    for x in range(longitud):
        
        check1Lectura =  cod1[f'linea{x}']['lectura'] 
        check2Lectura =  cod2[f'linea{x}']['lectura'] 

        check1escritura =  cod1[f'linea{x}']['escritura'] 
        check2escritura =  cod2[f'linea{x}']['escritura'] 

        checkLectura  = any(item in check1Lectura for item in check2Lectura)
        checkescritura = any(item in check1escritura for item in check2escritura)

        if checkLectura == False and checkescritura == False :
            contador += 1 
        else: break 

    if contador == longitud :
        print('Ambos codigo se puede ejecutar de manera simultanea') 

    else : 
        print(f'El codigo se puede ejecutar hasta la linea {contador} de cada codigo') 

compararCodigos(base1,base2)


# print(codigo2.read())

# print( "codigo1" ,  json.dumps(base1 , indent= 3 ))
# print( "codigo2" ,  json.dumps(base2 , indent= 3 ))

# print( base1 )

