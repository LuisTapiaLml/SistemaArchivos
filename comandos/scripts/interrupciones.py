# Díaz Ascos Jesus Gustavo
# Perez Tapia Jose Luis Enrique
# Trejo Martinez Jorge Joshua

import time
import random
na=((random.random())*100)+1
na_int=int(na)
pregunta="s"
print('{:^10}{:^10}'.format('#','Tamaño(Mb)'))
while pregunta=="s":
  for i in range(0,101):
    print('{:^10}{:^10}{}'.format(i,random.random()*100," Mb"))
    time.sleep(0.05)
    if (na_int==i):
      print("\nSe detuvo la ejecución porque tardó demasiado tiempo")
      pregunta=input("\n¿Quiere seguir con la ejecución? <s-n>: ")
      if pregunta=="n":
        print("\nLa ejecución no finalizó, intente de nuevo más tarde")
        break
  if i==100:
    print("\nEjecución finalizada exitosamente")
    break
