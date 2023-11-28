'''Proyecto filtrado de datos'''
'''Tener en cuenta que para sumar diccionarios se requiere el 
    pipe operator |'''


DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]


def run():
    py_devs = [worker['name'] for worker in DATA if worker['language'] 
    == 'python'] #nombre todos los desarrolladores de python
    platzi_w = [worker['name'] for worker in DATA if worker['organization'] 
    == 'Platzi'] #nombre emplados platzi
    adults = [person['name'] for person in DATA if person['age']>18]
    old = list(map(lambda worker: worker | 
    {"old":worker['age']>70},DATA)) #agregamos a los diccionario la llave 
                                    #old para aquellas personas que sean 
                                    #mayores a 70
    aold = [people | {'old':people['age']>70} for people in DATA]
    print(aold)


if __name__ == '__main__':
    run()