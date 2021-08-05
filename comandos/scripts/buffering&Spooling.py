# Díaz Ascos Jesus Gustavo
# Perez Tapia Jose Luis Enrique
# Trejo Martinez Jorge Joshua

import numpy as np
import time
np.warnings.filterwarnings('ignore', category=np.VisibleDeprecationWarning)
td=[]
for i in range(10001):
    fila=[]
    fila.append(i)
    fila.append(np.random.normal(15,4))
    td.append(fila)
datos_tamanio=np.array(td)[:,1]
media_tamanio=np.mean(datos_tamanio)
ordenar=datos_tamanio.tolist()
ordenar.sort()
for k in range(3,0,-1):
    print(f"Almacenando datos en el buffer... {k}sec")
    time.sleep(1)
print("\nTabla de datos, cuanto mayor tamaño, mayor prioridad(1): \n") 
print('{:^10}{:^10}  {:^10}'.format('#','Tamaño(bytes)', 'Prioridad'))
for j in range(1,10001):
    dato=ordenar.pop()
    if dato>=20:
        print('{:^10}{:^10.9f}   {:^10}'.format(j, dato, 1))
    elif  20>dato>15:
        print('{:^10}{:^10.9f}   {:^10}'.format(j, dato, 2))
    elif dato==15:
        print('{:^10}{:^10.9f}   {:^10}'.format(j, dato, 3))
    elif 10<dato<15:
        print('{:^10}{:^10.9f}   {:^10}'.format(j, dato, 4))
    elif dato<=10:
        print('{:^10}{:^10.9f}   {:^10}'.format(j, dato, 5))
print('{:^10}{:^10}'.format('Media de tamaño: ',media_tamanio))



