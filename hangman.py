import getpass
#mensaje de bienvenida

def establecer_palabra(intentos: int) -> str:
    print('Bienvenido al juego del ahorcado.\n\nA continuación escojerás la palabra para jugar y después tendrás 7 oportunidades para adivinar la palabra\n')
    
    #se utiliza getpass para volver invisible la palabra en la terminal
    palabra = getpass.getpass('Escribe tu palabra y presiona "Enter": ').strip().upper()
        
    guiones = ""
    
    for _ in palabra:
        guiones += "_ "
        
    guiones = guiones.strip()

    print(f'\n---------------------------------------\nLa palabra tiene {len(palabra)} letras:\n\n{guiones}\n\nTienes {intentos} intentos. Suerte!')
    
    return palabra
    
def jugar(palabra: str, intentos: int) -> int:
    letras_adivinadas = []
    
    while intentos > 0:
        
        mostrar = ""
        
        letra_escojida = input("\nEscoje una letra: ").upper()
    
        if len(letra_escojida) != 1:
            print("\nError. Escoje nuevamente")
            continue
        
        if letra_escojida in letras_adivinadas:
            print("\nLetra ya escojida anteriormente. Escoje nuevamente")
            continue
        
        if letra_escojida not in palabra:
            intentos -= 1
            print(f"\nIncorrecto! Te quedan {intentos} intentos")
            continue
            
        letras_adivinadas.append(letra_escojida)
        
        for letra in palabra:
            if letra in letras_adivinadas:
                mostrar += letra+" "
            else:
                mostrar += "_ "
                
        if "_" not in mostrar:
            break
        
        print(f"\n{mostrar}")
        
    return intentos
    

def resultado(palabra: str, intentos: int):
    print('\n------------------------------------------------------------------\n')
    if intentos == 0:
        print(f'Se te acabaron los intentos! La palabra era "{palabra}"\nMejor suerte la próxima vez!')
    else:
        print(f'Ganaste! La palabra es "{palabra}". Felicitaciones!')
        
    input(f'\nPresiona "Enter" para salir')
    
    
if __name__ == "__main__":
    intentos = 7
    
    palabra = establecer_palabra(intentos)
    
    intentos = jugar(palabra, intentos)
    
    resultado(palabra, intentos)
    