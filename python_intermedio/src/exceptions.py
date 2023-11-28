'''Excepciones y manejo de excepciones
    try: En el try se coloca el codigo que puede tirar error
    except: Es donde se maneja el error especifico, si se da otro tipo de error 
    el except no lo coge; en caso de dar este error especifico se va por este camino.
    raise: Es para elevar un error no detectado por Python
    finally: Es una instruccion que siempre se ejecuta haya sido lanzado un error o no.
    '''


def divisors(n):
    divs = []
    for i in range(1,n+1):
        if n%i == 0:
            divs.append(i)
        else: 
            pass
    return divs


def run(number):
    try:
        #number = int(input('Numero -> '))
        if number <= 0:
            raise Exception('Negativos y cero no permitidos.')
        divs = divisors(number)
        return(f'Los divisores de {number} son {divs}')
    except ValueError:
        print ('Solo se permiten numeros')
    
    except Exception as err:
        print(err)

if __name__ == '__main__':
    run()


