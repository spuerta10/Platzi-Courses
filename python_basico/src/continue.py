def run():
    for x in range(1000):
        #imprimir de 3 en 3
        if x %3 != 0:
            continue #salta instrucciones de abajo, vuelve a la cabeza del ciclo
        else:
            print(x)


if __name__ == '__main__':
    run()