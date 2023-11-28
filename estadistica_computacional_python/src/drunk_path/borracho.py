import random

class Borracho:
    
    def __init__(self, nombre):
        self.nombre = nombre
        

class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
         
    def camina(self): 
        #camina aleatoriamente entre 4 opciones
        #random.choice me elige una opcion aleatorio de una lista de opciones dadas
        return random.choice([(0,1), (0,-1), 
                              (1,0), (-1,0)])
    
    