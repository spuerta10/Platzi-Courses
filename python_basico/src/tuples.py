# las tuplas son una estructura de datos estatica la cual consume menos recursos tanto en tiempo como en espacio
# osea, las tuplas son mas rapidas y ocupan menos espacio que las listas dinamicas en Python
import time

def gen(limit):
    numbers = []
    for x in range(1, limit+1):
        numbers.append(x)
    return numbers

def time_tuple():
    tupla = tuple(gen(10000000))
    start = time.time()
    for x in tupla:
        x = x
    end = time.time()
    print(f'Para recorrer la tupla me demoro {(end - start)}')

def time_list():
    lista = gen(10000000)
    start = time.time()
    for x in lista:
        x = x
    end = time.time()
    print(f'Para recorrer la lista me demoro {(end - start)}')


def run():
    time_tuple()

if __name__ == '__main__':
    run()

