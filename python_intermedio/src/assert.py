'''Assert statements: assert condicion, mensaje de error'''

def divisors(n):
    divs = []
    for i in range(1,n+1):
        if n%i == 0:
            divs.append(i)
        else: 
            pass
    return divs


def run():
    number = input('Numero -> ')
    #si es numero True, si no False
    assert number.isnumeric() and int(number)>0,"Solo numeros positivos permitidos" 
    number = int(number)
    divs = divisors(int(number))     
    print(f'Los divisores de {number} son {divs}')

if __name__ == '__main__':
    run()