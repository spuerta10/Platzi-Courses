'''Trabajar con archivos en python: Principalmente tres modos de apertura
    R -> Lectura
    W -> Escritura (sobrescribir)
    A -> Escritura (aregar al final)
    with open ("ruta", "r"-"w"-"a") as file
    with: Controla el flujo del archivo por si este se cierra de 
          forma abrupta no se rompa'''

from exceptions import run as divs


def r(path): #funcion para leer
    nums = []
    #abro el archivo 
    with open(f"{path}","r",encoding = "utf-8") as text:
        #bloque de codigo del archivo
        for line in text:
            nums.append(int(line))
    return nums


def w(path): #funcion para escribir
    nums = r(path)
    with open(f"{path}", "a", encoding = "utf-8") as text:
        #bloque de codigo del archivo
        for n in nums:
            text.write(f"{divs(n)}\n")


def run():
    w("./nums.txt")


if __name__ == '__main__':
    run()