'''Todo el posible codigo de modificacion de un diccionario en una sola linea
    {key: value for element in iterable if condition}
    element: Cada uno de los elementos a poner en la lista
    for element in iterable: Ciclo 
    if condition: Condicion para filtrar los elementos del ciclo
    Para cada elemento en el ciclo, se guarda el elemento solo si este
    cumple la condicion.'''
def run():
    dicc = {}
    numbers = {n: n**3 for n in range(1,101) if n%3!=0}
    squares = {n: round((n**0.5),2) for n in range (1,1001)}
    # for n in range(1,101):
    #     if n%3!=0:
    #         dicc[n] = n**3
    print(squares)
if __name__ == '__main__':
    run()
