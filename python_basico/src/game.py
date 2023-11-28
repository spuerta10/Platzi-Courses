import random as r

def run():
    print('''Bienvenido al juego.
             El juego consiste en que debes de adivinar el numero que he generado para ti.
             Tienes 10 oportunidades de adivinarlo, de lo contrario perdiste.''')
    number = r.randint(1,100)
    mistake = 0
    while mistake != 10:
        guess = int(input("Digita el numero -> "))
        if guess == number:
            print("Bien hecho has acertado!")
            break
        if guess != number:
            mistake += 1
            if number > guess:
                print(f"Es un numero mayor a {guess}")
            else:
                print(f"Es un numero menor a {guess}")
    if mistake == 10:
        print("Has perdido, lloremos.")


if __name__ == '__main__':
    run()
        
        
