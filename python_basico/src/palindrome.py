


def palindrome(word):
    word = word.replace(" ","").lower() #el replace para remplazar
    if word[::-1] == word:
        return True 
    else:
        return False

if __name__ == '__main__':
    while True:
        word = input("Digite una palabra")
        if palindrome(word) == True:
            print(f"La palabra {word} es palindromo")

        else:
            print(f"La palabra {word} no es palindromo")

        if int(input("Digite 0 para parar, 1 para seguir")) == 0:
            break
        else:
            pass
