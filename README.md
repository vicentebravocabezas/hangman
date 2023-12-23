# El Ahorcado

El juego "El Ahorcado" desarrollado en Python. El proyecto fue finalizado y entregado el día 2023-12-22.

Está diseñado para mínimo dos jugadores en donde el objetivo es que uno debe colocar la palabra en secreto y los demás deben adivinar dentro de un número predeterminado de intentos. 

## Reglas del juego

Al iniciar, un jugador debe ingresar una palabra para poder empezar el juego.

Despues, se le mostrará la cantidad de letras y se le dará 7 intentos para adivinar las letras.

Al final se le indicará al jugador si ganó o perdió junto con la palabra ingresada al inicio.

## Instrucciones de ejecución

El programa utiliza una sola libreria:

```py
import getpass
```

Este es parte de la libreria estandar de Python, no es necesario instalarla.

Solamente es necesario ejecutar el script `hangman.py`

## Estructura del Programa

### Punto de entrada

El punto de entrada del programa inicia estableciendo el número de intentos en una variable. Después ejecuta las siguientes funciones en orden:

### Establecer palabra

El programa da la bienvenida a los jugadores se le pedirá a uno que ingrese la palabra. El programa utiliza la librería `getpass` para permitir al jugador ingresar la palabra en secreto sin que se visualice en la consola. Después de esta acción, el programa mostrará el número de letras de la palabra, el número de intentos para adivinar, y una fila con subguiones por cada letra de la palabra escrita.

### Desarrollo del juego

Se establece una lista en donde se almacenarán las letras que los usuarios adivinan. 

Se inicia el bucle principal con la condición de que el número de intentos sea mayor a 0.

El programa solicita al jugador que adivine la letra y realiza revisiones y condicionales para asegurar que el usuario ingrese información correcta y que no haya sido ya ingresada anteriormente. Las letras ingresadas se guardan en la lista declarada al inicio de la función.

Se revisa si la letra ingresada está en la palabra. Si no está se decrementa el número de intentos y se reinicia el bucle.

Se muestra en la consola la palabra con las letras adivinadas y subguiones para las que aún no se han adivinado.

Al final del bucle se revisa si existen subguiones en la variable que se imprime a la consola.

Al terminar, la función retorna la variable con el número de intentos.

### Resultado y mensaje final

Esta función recibe el número de intentos y revisa si es 0. De ser el caso, se infiere que el jugador perdió, de no ser el caso, se infiere que el jugador ganó y se muestra el mensaje correspondiente.