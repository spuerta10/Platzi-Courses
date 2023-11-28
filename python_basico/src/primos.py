def run(number):
    #manejo el caso donde el numero sea 1
    if number == 1: 
        return False
    else:
        #mi numero es primo si y solo si se divide entre 1 y entre si mismo
        #busco los casos donde el numero se pueda dividir entre mas numeros que 1 y si mismo
        for x in range(2, number): #me voy desde el 2 hasta numero -1
            if number % x == 0:
                return False
        return True
    

if __name__ == '__main__':
    print(f'{run(22)}') #imprimo si es primo = True o no = False 