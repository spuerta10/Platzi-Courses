class Coordenada:
    
    def __init__(self, x,y):
        self.x = x
        self.y = x
        
    def mover(self, delta_x, delta_y):
        #delta x, y quiere decir cuanto nos estamos moviendo hacia la x y cuanto hacia la y
        return Coordenada(self.x+ delta_x, self.y + delta_y)

    def distancia(self, otra_coordenada):
        #uso pitagoras para calcular distancias entre dos puntos
        delta_x = self.x - otra_coordenada.x
        delta_y = self.y - otra_coordenada.y
        return (delta_x**2 + delta_y**2)**1/2