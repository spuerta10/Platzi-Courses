#diccionario con pais y numero de habitantes
def run():
    pais = {
        'Colombia': '50 millones',
        'Chile': '18 millones',
        'Mexico': '127 millones'
    }
    #para ver solo las keys del dict
    for x in pais.keys():
        print(x)
    
    for x in pais.values():
        print(x)

    for x, y in pais.items():
        print(f"{x} tiene {y} de habitantes")


if __name__ == '__main__':
    run()