import random
import math
import matplotlib.pyplot as plt
from numpy import size

class Point():
    
    number = 1
    
    def __init__(self, x: float, y:float):
        self.__x = x
        self.__y = y
        self.__number = Point.number
        Point.number += 1
        
        
    def __str__(self) -> str:
        return f"({self.__x},{self.__y})"
    
    
    def get_belongs(self):
        return self.__belongs
    
    
    def get_number(self):
        return self.__number
    
    
    def get_x(self):
        return self.__x
    
    
    def get_y(self):
        return self.__y
    
    
    def distance(self, cluster):
        '''Retorna la distancia del punto al cluster'''
        cluster_point_distance = math.sqrt(((cluster.get_x() - self.__x)**2) + ((cluster.get_y() - self.__y)**2)) #punto x1 y1, cluster x2 y2
        return cluster_point_distance
    
    
    def str_distance(self, cluster):
        '''Retorna mensaje de la distancia del punto al cluster'''
        cluster_point_distance = math.sqrt(((cluster.get_x() - self.__x)**2) + ((cluster.get_y() - self.__y)**2)) #punto x1 y1, cluster x2 y2
        return f"The distance between the point {self.__number} and the cluster {cluster.get_name()} is: {cluster_point_distance} cm"
    
    
    def belongs_to(self, cluster_a, cluster_b):
        distance_to_cluster_a = self.distance(cluster_a)
        distance_to_cluster_b = self.distance(cluster_b)
        if distance_to_cluster_a == distance_to_cluster_b:
            #si la distancia entre los puntos es la misma dejamos que el azar decida a que cluster pertence el punto en cuestion
            self.__belongs = f"cluster {random.choice([cluster_a, cluster_b]).get_name()}"
        elif distance_to_cluster_a > distance_to_cluster_b:
            self.__belongs = f"cluster {cluster_b.get_name()}"
        else:    
            self.__belongs = f"cluster {cluster_a.get_name()}"
        return None
    
    
class Cluster:
    def __init__(self, x, y, name):
        self.__x = x
        self.__y = y
        self.__name = name


    def __str__(self):
        return f"({self.__x},{self.__y})"


    def get_x(self):
        return self.__x
    
    
    def get_y(self):
        return self.__y
    
    
    def get_name(self):
        return self.__name
    
   
def __before_cluster_plot(points:list, clusters:list):
    points_x = [point.get_x() for point in points]
    points_y = [point.get_y() for point in points]
    plt.figure(figsize = (10,23))
    plt.title("Before getting aligned with a cluster")
    plt.scatter(points_x, points_y, color = "lightgreen")
    clusters_x = [cluster.get_x() for cluster in clusters]
    clusters_y = [cluster.get_y() for cluster in clusters]
    plt.scatter(clusters_x, clusters_y, color = "cornflowerblue", s = [95,95]) #s para modificar el tamaño de la visualizacion de los clusters  
    for cluster in clusters:
        plt.annotate(cluster.get_name(), (cluster.get_x(), cluster.get_y())) 
        
    return None
 
 
def __after_cluster_plot(points:list, clusters:list):
    points_x_cluster_a = [point.get_x() for point in points if point.get_belongs() == "cluster a"]
    points_y_cluster_a = [point.get_y() for point in points if point.get_belongs() == "cluster a"]
    points_x_cluster_b = [point.get_x() for point in points if point.get_belongs() == "cluster b"]
    points_y_cluster_b = [point.get_y() for point in points if point.get_belongs() == "cluster b"]
    cluster_a_x = [cluster.get_x() for cluster in clusters if cluster.get_name() == "a"]
    cluster_a_y = [cluster.get_y() for cluster in clusters if cluster.get_name() == "a"]
    cluster_b_x = [cluster.get_x() for cluster in clusters if cluster.get_name() == "b"]
    cluster_b_y = [cluster.get_y() for cluster in clusters if cluster.get_name() == "b"]
    plt.figure(figsize=(10,23))
    plt.title("After getting aligned with a cluster")
    plt.scatter(points_x_cluster_a, points_y_cluster_a, color = "cornflowerblue")
    plt.scatter(cluster_a_x, cluster_a_y, color = "cornflowerblue", s = 95)
    plt.scatter(points_x_cluster_b,points_y_cluster_b, color = "lightgreen")
    plt.scatter(cluster_b_x,cluster_b_y, color = "lightgreen", s = 95)
    for cluster in clusters:
        plt.annotate(cluster.get_name(), (cluster.get_x(), cluster.get_y())) 
    
    return None
    
    
def plot(points: list, clusters):
    __before_cluster_plot(points, clusters)
    __after_cluster_plot(points, clusters)
    plt.show()


if __name__ == "__main__":
    names = ["a", "b"]
    clusters = [Cluster(random.randint(0,50), random.randint(0,50), name = names[x]) for x in range (2)]
    points = [Point(random.randint(9,32), random.randint(2,56)) for x in range (0,21)]
    for point in points:
        print(point.str_distance(clusters[0]))
        print(point.str_distance(clusters[1]))
    
    print("\n\n\n----------------------")
    for point in points:
        point.belongs_to(clusters[0], clusters[1])
        print(f"point number {point.get_number()} belongs to {point.get_belongs()}")
        
    plot(points=points, clusters=clusters)