def gioco(vite):
    num_a =  5
    num = int(input("inserisci un numero: "))
    if num < 0 or num > 10:
        vite -= 1
        print("Numero non valido, hai perso una vita")

        return vite

    elif num_a > num:
         vite -= 1
         print("Il numero inserito è inferiore al sistema, hai perso una vita")
         return vite

    elif(num_a == num):
        print("Es un empate")

    else:
        print("Bravo!!  hai vinto ")

def main():
    print("""
    Il gioco consiste in scrivere un nuemero maggiore a quello del sistema tra 1 e 10, hai 3 intenti per provare.
    Buona fortuna!
    """)
    vite = 3 

    while(True):
        if vite == 0:
            print("Fine dil gioco")
            break
        vite = gioco(vite)
        print("Ti rimangono: " + str(vite) + " vite.")


if __name__ =='__main__':
    main()
