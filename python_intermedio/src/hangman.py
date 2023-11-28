'''Primera version cutre de the hangman game
    Santiago Puerta'''


import random


def letters(r_word):
    letters = [letter for letter in r_word]
    return letters


def to_str(letters): #funcion para pasar una lista a solo un string
    word = ""
    for letter in letters:
        word += letter
    return word


def r(path): #funcion para leer el archivo de palabras
    words = []
    try:
        with open(f"{path}", "r", encoding = "utf-8") as text:
            for word in text:
                words.append(word.replace('\n',''))
        return words
    except ValueError as ve:
        print(ve)
    

def run():
    words = r("./words.txt")
    w_index = random.randint(0,len(words))
    r_word = words[w_index] #palabra aleatoria
    l = letters(r_word) #lista de letras de mi palabra
    check = letters(r_word) #lista para saber cuando advine la palabra
    guessed = ['_' for letter in l] #lista de letras adivinadas
    print("Guess the word!") #muestro letras de la palabra
    tries = 0
    print(str(guessed))
    while True:
        if guessed == check:
            print(f"Congrats you've won! \n You took {tries} tries to made it")
            try:
                to_guess = to_str(check) #palabra adivinada
                words.pop(words.index(to_guess)) #quito la palabra adivinada
                                                 #de mi lista de palabras
            except ValueError as ve:
                print(ve)
            break
        else:
            guess = input(f'Write a letter -> ')
            try:
                index = l.index(guess)
                guessed[index] = guess
                l[index] = '.'
                print(guessed)
            except ValueError as err:
                tries += 1
                pass
    

if __name__ == '__main__':
    run()
