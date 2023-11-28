'''Funciones anonimas o lambda functions: Son funciones las cuales no
    poseen un variable = nombre/identificador su expresion debe de ser 
    plasmada en una sola linea de codigo
    lambda parametros: expresion'''


import random

def run():
    r_list = lambda list: [random.randint(0,99) for n in range(0,100)]
    print(r_list([])) #invocar a la variable que contiene lambda


if __name__ == '__main__':
    run()



