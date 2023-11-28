#modulo y fucion para copiar elemento anidadas, diccionario de diccionarios, lista de lista, lista de diccionarios, etc..
from copy import deepcopy

def sets():
    set_countries = {
        'col', 'mex', 'usa', 'pe'
    }

    countries_two = {
        'ar', 'bol', 'col', 'ur'
    }

    #saber si un elemento esta dentro del conjunto
    'col' in set_countries

    #añadir al conjunto
    set_countries.add('pe')

    #actualizar un conjunto
    set_countries.update({'ar', 'ecu'})

    #quitar elemento del conjunto
    set_countries.remove('col') #tira error si el elemento no existe
    set_countries.discard('ar') #no tira error si el elemento no existe

    #dejar vacio el conjunto
    set_countries.clear()


    #union de conjuntos
    set_union = set_countries.union(countries_two)
    set_union = set_countries | countries_two

    #interseccion de conjuntos
    set_interseccion = set_countries.intersection(countries_two)
    set_interseccion = set_countries & countries_two

    #diferencias
    set_diferencia = set_countries.difference(countries_two)
    set_diferencia = set_countries - countries_two

    #diferencia simetrica: hacer una union descartando la interseccion de los conjuntos
    set_simetrica = set_countries.symmetric_difference(countries_two)
    set_simetrica = set_countries ^ countries_two

def list_dict_comprehensions():
    #list comprehension sin condicional
    evens = [element for element in range(1,30,2)] #range de 1 a 30 con saltos de a 2
    #list comprehension con condicional
    not_evens = [element for element in range(1,30) if element%2!=0]

    #dict comprehension
    dict_evens = {i:i*2 for i in range(1,30,2)}
    #dict comprehension con condicionales
    dict_not_evens = {i:i for i in range(1,30) if i%2!=0}

    #unir una lista con otra
    names = ["santiago", "miguel", "tomas"]
    ages = [21, 20, 32]
    print(next(zip(names, ages))) #objeto iterador

def lambda_funct():
    #lambda argumento_de_entrada : salida
    increment = lambda x:x+1
    
    #lambda con condicionales
    lambda_evens = lambda number:number if number%2==0 else None 
    
    print(lambda_evens(21))

def map_funct():
    #funcion principal es hacer transformaciones a una lista dada de elementos
    numbers = [i for i in range(1,10)]
    even_nums = list(map(lambda x:x*2, numbers)) #multiplico por 2 todos los elementos de la lista  

    #map y lambda con mas de un parametro, las listas no deben de ser de la misma longitud para el funcionamiento
    another_list = list(map(lambda x,y:y+x, numbers, even_nums))
    print(another_list)
    
    TAX_PERCENTAGE = 0.19
    
    items = [
        {'product': 'camisa','price': 100},
        {'product': 'pantalones','price': 50},
        {'product': 'zapatos','price': 250}
        ]
    prices = list(map(lambda item:item['price'], items))
    print(prices)

    #podemos hacer append a un diccionario de la siguiente forma {'hola':12} | {'chao':10}
    taxes = list(map( lambda x: x|{'tax': x['price']*0.19} ,items))
    
    #para listas y diccionarios al crear una nueva lista = a la vieja ambas listas y diccionarios apuntan a la misma posicion de memoria
    
    #para poder crear una copia que apunte a una nueva posicion de memoria de un elemento anidado
    #en caso de que el elemento no sea anidado usar element.copy()
    new_taxes = deepcopy(taxes)

    print(taxes)
    
def filter_funct():
    #seleccionar ciertos elementos para que pertenezcan a una nueva lista
    numbers = [i for i in range(0,10)]
    #filter y map crean una nueva lista
    even_nums = list(filter(lambda x: x%2==0, numbers))
    
    matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
    ]    
    
    wins = list(filter(lambda x: x['home_team_result'] == "Win",matches))
    print(wins)



def reduce_funct():
    #reduce sirve para sacar una conclusion dado un elemento iterable,
    #tranformar todo un elemento iterable a un solo valor
    from functools import reduce
    numbers = [i for i in range(0,10)]
    #reduce funciona como una funcion recursiva, es por esto que debemos de tener dos variables para hallar la sumatoria de elementos
    result = reduce(lambda counter, item: counter + item, numbers) #sumatoria de elementos de un array
    print(result)


def iterables():
    #iter permite controlar la forma en la que se ejecuta un iterador
    #esto nos ayuda a no ocupar tanta memoria, al no haber mas iterables se genera el StopIertation error
    iter_range = iter(range(1,11))
    
    pass


def handle_errors():
    #El bloque else se ejecuta cuando todo lo del bloque ‘try’ se ejecuta correctamente, es decir, sin excepciones.
    #El bloque finally se ejcuta haya o no excepciones en el bloque ‘try’, es decir, que su ejecución es obligatoria
    try:
        pass
    #capturando diferentes tipos de errores
    except Exception as error:
        pass
    except ValueError as error:
        pass
    except NotADirectoryError as error:
        pass
    else:
        pass
    finally:
        pass


def text_manipulation():
    #abrir y leer archivo de texto 
    file = open('')
    file.read() #carga todo el archivo en memoria
    file.readline() #lee linea a linea el  txt, carga una linea en memoria
    for line in file:
        print(line) #se lee el archivo linea a linea
    file.close() #cerrar el archivo manualmente
    
    '''
    Diferentes tipos de permisos a la hora de abrir archivos
    r -> abre un archivo solo para lectura. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
    rb -> abre un archivo solo para lectura en formato binario. El puntero al archivo esta localizado al comienzo del archivo. Este es el modo predeterminado de la función.
    r+ -> abre un archivo para escritura y lectura. El puntero del archivo está localizado al comienzo del archivo.
    w -> abre un archivo solo para escritura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
    wb -> abre un archivo solo para escritura en formato binario. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
    w+ -> abre un archivo para escritura y lectura. Sobreescribe el archivo si este ya existe. Si el archivo no existe, crea un nuevo archivo para escritura.
    a -> abre un archivo para anexo. El puntero del archivo esta al final del archivo si este existe. Es decir, el archivo está en modo anexo. Si el archivo no existe, crea un nuevo archivo para escritura.
    '''
    
    
    
    with open('file_path', 'r') as file:
        '''
        abre el archivo y cuando termninan las operaciones especificadas
        lo cierra automaticamente
        '''
        #hacer las operaciones 
        file.write('hola que mas') #escribir en el archivo
        pass


if __name__ == "__main__":
    reduce_funct()