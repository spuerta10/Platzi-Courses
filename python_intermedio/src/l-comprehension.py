'''Todo el posible codigo de modificacion de una lista en una sola linea
    [element for element in iterable if condition]
    element: Cada uno de los elementos a poner en la lista
    for element in iterable: Ciclo 
    if condition: Condicion para filtrar los elementos del ciclo
    Para cada elemento en el ciclo, se guarda el elemento solo si este
    cumple la condicion.'''
def run():
    naturals = [x**2 for x in range(1,101) if x%3 !=0] #list comprehension
    multiples = [n for n in range(1,10000) if n%4==0 and n%6==0 and n%9==0]
    # for x in range(1,101):
    #     if x %3 != 0:
    #         naturals.append(x**2)
    #     else:
    #         pass
    print(multiples)

if __name__ == '__main__':
    run()
