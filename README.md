# **Sistema de Archivos**

## Descripción

Simulación de sistema de archivos.
Se pueden crear carpetas y archivos (unicamente texto plano)
[URL del repositorio ](https://github.com/LuisTapiaLml/SistemaArchivos.git)

---

## Integrantes Del Equipo

+ Díaz Arcos Jesus Gustavo
+ Perez Tapia Jose Luis Enrique
+ Trejo Martinez Jorge Joshua

---

## Reglas

La forma basica de los comandos esta compuesta por tres partes, dependido el modificador se le pueden agregar o disminuir argumentos al comando

**<span style="color:#f08d49"> comando </span>
<span style="color:#62c699">modificador </span>
<span style="color:#418ad4">path</span>**  

*Ejemplo:* 

**<span style="color:#f08d49"> dir </span>
<span style="color:#62c699">crear </span>
<span style="color:#418ad4">root/carpeta1/carpeta2</span>** 

**Ejemplo de rutas aceptadas**

`./carpeta/carpeta2` <br>
` ../carpeta/carpeta2 `</br>
`./../carpeta/carpeta2 `</br>
`root:/carpeta/`

---

## **comandos**

+ ## **dir**
    Comando para menjar las carpetas dentro del sistema de archivos

    | Modificador | Descripción | Ejemplo | notas |
    | ----------- | ----------- | ----------- | ----------- |
    | crear | Crea una carpeta o subcarpetas siguiendo el </br> path del tercer argumento del comando | ` dir crear carpeta/carpetaNueva/`   ||
    | ir | navega a una carpeta siguiendo el </br> path del tercer argumento del comando | ` gir ir ../carpeta2 ` ||
    | eliminar | elimina una carpeta siguiendo el </br> path del tercer argumento | ` dir eliminar carpeta/carpetaNueva ` | <span style="color:#ff8000"> Eliminara todo el contido de la carpeta</span>|
    | renom | renombra una carpeta  | ` dir renom  nombreActual  nuevoNombre ` | La carpeta a renombrar debe ser hijo inmediato de la carpeta actual |
    | copiar | copia una carpeta y su contenido de </br> la primer ruta dada a la segunda | ` dir copiar carpeta/carpeta2  root:/ ` | si ya existe una carpeta con el mismo nombre que la ruta destino el contenido se reemplazara |
    | mover | mueve  una carpeta y su contenido de </br> la primer ruta dada a la segunda | ` dir mover ./carpeta2 root:/ ` ||
    | ver | muesta el contenido de la ruta actual | ` dir ver ` ||

+ ## **file** 
    Comando para manejar archivos del sistema

    | Modificador | Descripción | Ejemplo | notas |
    | ----------- | ----------- | ----------- | ----------- |
    | crear | crear un archivo en la ruta proporcionada  |  `file crear root:/carpeta/archivo.txt  "contenido" ` | El contenido es opcional y </br> debe estar entre comillas dobles |
    | eliminar | eliminar un archivo siguiente el path del </br> tercer argumento  | `file eliminar root:/carpeta/archivo.txt`  | |
    | renom | rembra un archivo  | `file renom archivo.txt nuevoNobre.txt` | el archivo a renombrar debe ser hijo inmediato de </br> la carpeta actual  |
    | capiar | copia un archivo de la primer ruta a la segunda | `file copiar ./archivo.txt  ./../`  |  |
    | mover | mueve un archivo de la primer ruta a la segunda  | `file mover ./archivo.txt  ./../`   |  |
    | mod | modifica el contenido de un archivo  | `file mod  "nuevo contenido" `   | sustituye el contenido del archivo , </br> el contenido debe estar entre comillas dobles |
    | leer | Muestra el contenido de </br> un archivo de la ruta proporcionada  | `file leer root:/carpeta/archivo.txt ` |  |

+ ## **Comandos adicionales** 
    | Comando | Descripcion | Ejemplo |
    | ----------- | ----------- | ----------- |
    | tree | muestra el arbol de elementos en el path actual | `tree` |
    | cache | Ejecuta el script del ejecicio de cache |  |
    | concurrencia | Ejecuta el script del ejecicio de concurrencia |  |
    | buffering | Ejecuta el script del ejecicio de buffering |  |
    | interrupciones | Ejecuta el script del ejecicio de interrupciones |  |
