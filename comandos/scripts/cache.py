# Díaz Ascos Jesus Gustavo
# Perez Tapia Jose Luis Enrique
# Trejo Martinez Jorge Joshua


import random
import time
#nivel1
print("\t   NIVEL 1")
print('{:^10}{:^20} {:^10}{:^20}'.format('Indice','Dato', 'Tamaño',' #Accesos'))
time.sleep(.10)
tamanio_total=0
indice=0
acceso_a=0
acceso_b=0
acceso_c=0
while tamanio_total<=128:
    tamanio=((random.random())*10)+1
    tamanio_total=tamanio_total+tamanio
    indice=indice+1
    letras='abc'
    dato=random.choice(letras)
    if dato=='a':
        acceso_a=acceso_a+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_a))
        time.sleep(.10)
    if dato=='b':
        acceso_b=acceso_b+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_b))
        time.sleep(.10)
    if dato=='c':
        acceso_c=acceso_c+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_c))        
        time.sleep(.10)
if tamanio_total>128:
    tamanio_total=tamanio_total-tamanio
    print(f"Caché en el nivel 1: {tamanio_total} kb")
    time.sleep(1)

#nivel2
print("\n\t   NIVEL 2")
print('{:^10}{:^20} {:^10}{:^20}'.format('Indice','Dato', 'Tamaño',' #Accesos'))
time.sleep(.10)
tamanio_total=0
indice=0
acceso_a=0
acceso_b=0
acceso_c=0
while tamanio_total<=1000:
    tamanio=((random.random())*100)+1
    tamanio_total=tamanio_total+tamanio
    indice=indice+1
    letras='abc'
    dato=random.choice(letras)
    if dato=='a':
        acceso_a=acceso_a+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_a))
        time.sleep(.10)
    if dato=='b':
        acceso_b=acceso_b+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_b))
        time.sleep(.10)
    if dato=='c':
        acceso_c=acceso_c+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_c))        
        time.sleep(.10)
if tamanio_total>1000:
    tamanio_total=tamanio_total-tamanio
    print(f"Caché en el nivel 2: {tamanio_total} kb")
    time.sleep(1)
#nivel 3
print("\n\t   NIVEL 3")
print('{:^10}{:^20} {:^10}{:^20}'.format('Indice','Dato', 'Tamaño',' #Accesos'))
time.sleep(.10)
tamanio_total=0
indice=0
acceso_a=0
acceso_b=0
acceso_c=0
while tamanio_total<=50000:
    tamanio=((random.random())*1000)+1
    tamanio_total=tamanio_total+tamanio
    indice=indice+1
    letras='abc'
    dato=random.choice(letras)
    if dato=='a':
        acceso_a=acceso_a+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_a))
        time.sleep(.10)
    if dato=='b':
        acceso_b=acceso_b+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_b))
        time.sleep(.10)
    if dato=='c':
        acceso_c=acceso_c+1
        print('  {:^10}    {:^20} {:^10.2f}{}{:^20}'.format(indice,dato, tamanio,'kb',acceso_c))        
        time.sleep(.10)
if tamanio_total>50000:
    tamanio_total=tamanio_total-tamanio
    print(f"Caché en el nivel 3: {tamanio_total} kb")







