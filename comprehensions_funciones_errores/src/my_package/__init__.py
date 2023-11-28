'''
Desde la version 3.3 e inferiores de python
debiamos de declarar este archivo para que python reconociera
a la carpeta como paquete.


Tambien sirve para incializar variables e importaciones al paquete

Una vez que se importa el paquete el __init__.py del mismo corre

Tambien pueden ser usados para la creacion de name spaces
'''



#una vez importado el paquete puedo acceder al modulo de aritmetica sin la necesidad del import explicito del mismo
#mypackage.aritmetics.suma() importacion usando namespace
import my_package.aritmetics 

