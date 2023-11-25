import getpass
#mensaje de bienvenida
print('Bienvenido al juego del ahorcado.\n\nA continuación escojerás la palabra para jugar y después tendrás 7 oportunidades para adivinar la palabra\n')

intentos = 7
#se utiliza getpass para volver invisible la palabra en la terminal
word = getpass.getpass('Escribe tu palabra: ').strip().upper()

print(f'La palabra que escojiste es "{word}" y tienes {intentos} intentos. Suerte!')