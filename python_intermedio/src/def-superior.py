'''Funciones de orden superior: Son funciones que reciben como parametro
    a otra funcion'''

'''filter: devuelve True o False si el valor se encuentra en los criterios
de busqueda, en caso de que no el valor no sera devuelto y la lista 
se reduce
    map: funciona parecido al filter, pero este no puede eliminar valores
    del arreglo dado
    from functools import reduce: reduce toma como parametro cualquier
    objeto iterable y lo reduce a un unico valor.'''


from functools import reduce


alist = [1,2,4,7,10,11,13,15,16]
odd = list(filter(lambda x: x%2 !=0, alist)) #devuelve alist con todos los
                                             #valores impares

squares = list(map(lambda x:x**2,alist)) #devuelve los numeros de alist
                                         #al cuadrado

all_multipled = reduce(lambda a,b: a*b, alist) #devuelve el resultado
                                               #de multiplicar todos los
                                               #numero de alist