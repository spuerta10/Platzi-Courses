from typing import Any


def collections():
    return """
    grupo de 0 o mas elementos que se pueden tratar como unidad conceptual
    Tipos de colecciones:
        - Dinamicas: Pueden variar su tamaño
        - Inmutables: No varian su tamaño
    
    Estructuras lineales:
        - ordendas por posicion
        - Solo el primer elemento no tiene predecesor
    
    Jerarquicas:
        - Ordenadas como arbol invertido
        - Solo el primer elemento no tiene predecesor
        - Padres (predecesores) e hijos (sucesores)
        
    Grafos:
        - Cada dato puede tener vecinos o no tenerlos
        - Los elementos se relacionan entre si con n relaciones
        
    Colecciones en python:
        - listas
        - tuplas
        - conjuntos / sets
    """
    
    
    
class Array:
    def __init__(self, capacity, fill_value=None) -> None:
        self.items = list()
        for _ in range(capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    
    def __iter__(self):
        #retornar un iterador de la lista de elementos
        return iter(self.items)
    
    def __getitem__(self, index):
        #obtener un elemnto particular del array
        return self.items[index]
    
    def __setitem__(self, index, new_item):
        #metodo para reemplazar un elemento
        self.items[index] = new_item
        
    def __sum__(self):
        #suma de todos los elementos del array
        return sum(self.items)
    
    
class Matrix:
    def __init__(self, rows, cols, fill_value=None) -> None:
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(cols, fill_value)
        
    def get_height(self):
        return len(self.data)
    
    def get_width(self):
        return len(self.data[0])
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __str__(self):
        ans = ""
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                ans += str(self.data[row][col]) + " "
            
            ans += "\n"
            
        return ans
    

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next



class LinkedList:
    """
    Data: valor almacenado en los nodos
    Next: referencia al siguiente nodo
    Previous: referencia al nodo anterior
    
    Los nodos se encuentran repartidos en la memoria, no son continuos
    
    El HEAD de la linkedList es el ultimo nodo insertado
    """
    
    def __init__(self):
        self.head = None
        self.size = 0 

    def add_to_start(self, data):
        """Inserta un nodo al inicio."""
        self.head = Node(data, self.head)
        print(f"Nodo {self.head.data} añadido a la cabezera.")
        self.size += 1

    def append(self, data):
        """Añade un nodo nuevo al final."""
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            probe = self.head
            while probe.next:
                probe = probe.next
            probe.next = node
        print(f"Nodo {node.data} añadido a la cola.")
        self.size += 1

    def insert(self, data, index):
        """Inserta un nodo segun indice."""
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None or index <= 0:
                self.head = Node(data, self.head)
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next != None:
                    probe = probe.next
                    index -= 1
                probe.next = Node(data, probe.next)
            print(f"Nodo {data} añadido.")
            self.size += 1

    def replace(self, data, new_data):
        """Reemplaza un nodo por uno nuevo."""
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            probe.data = new_data
            print(f"El nodo {data} ha sido reemplazado por {new_data}")
        else:
            print(f"The target item {data} is not in the linked list")

    def delete(self, index):
        """Elimina nodo en posición dada."""
        if index > self.count_nodes():
            print("El indice supera la cantidad de nodos")
        else:
            if self.head is None:
                print("No hay nodos que eliminar.")
            elif self.head.next is None:
                print(f"Nodo: {self.head.data} eliminado.")
                self.head = None
                self.size -= 1
            else:
                probe = self.head
                index -= 1
                while index > 1 and probe.next.next != None:
                    probe = probe.next
                    index -= 1
                removed_item = probe.next.data
                probe.next = probe.next.next
                print(f"Nodo:{removed_item} eliminado.")
                self.size -= 1

    def pop(self):
        """Elimina ultimo nodo."""
        data = self.head.data
        if self.head.next is None:
            self.head = None
        else:
            probe = self.head
            while probe.next.next != None:
                probe = probe.next
            data = probe.next.data
            probe.next = None
        self.size -= 1
        print(f"Ultimo nodo {data} eliminado.")

    def search(self, data):
        """Busca nodo especificado."""
        probe = self.head
        while probe != None and data != probe.data:
            probe = probe.next
        if probe != None:
            print(f"El nodo {data} ha sido encontrado.")
            return probe
        else:
            print(f"El nodo {data} no se encuentra en el grafo.")

    def count_nodes(self):
        """Imprime cantidad de nodos."""
        return self.size

    def print(self):
        """Imprime cada nodo."""
        probe = self.head
        while probe != None:
            print(probe.data)
            probe = probe.next
    
    def clear(self):
        self.head = None
        self.size = 0
        

class circularLinkedList:
    '''
    El ultimo nodo hace referencia al primer nodo que se instancio
    '''
    def __init__(self):
        self.head = None

    def traverse(self, starting_point=None):
        if starting_point is None:
            starting_point = self.head
        node = starting_point
        while node is not None and (node.next != starting_point):
            yield node
            node = node.next
        yield node

    def print_list(self, starting_point=None):
        nodes = []
        for node in self.traverse(starting_point):
            nodes.append(str(node))
        print(" -> ".join(nodes))
        
        
class TwoWayNode(Node):
    def __init__(self, data, previous = None, next=None):
        Node.__init__(self, data, next)
        self.previous = previous
        

class circleDoubleLinkedList():
    def __init__(self):
        self.head = TwoWayNode(None,None,None)
        self.tail = self.head
        self.size = 0

        self.head.next = self.tail
        self.head.previous = self.tail


    def range(self, start, stop):
        # * Creación de los nodos enlazados (linked list)
        self.head = TwoWayNode(start, next=None, previous=None)
        self.tail = self.head
        self.size = 1

        for data in range(start+1, stop):
            self.tail.next = TwoWayNode(data, previous=self.tail)
            self.tail = self.tail.next
            self.size += 1

        self.tail.next = self.head
        self.head.previous = self.tail

    def __str__(self):
        # * Recorrer e imprimir valores de la lista
        probe = self.head
        result = ''
        while probe.next != self.head:
            result += f'{probe.data} '
            probe = probe.next
        result += f'{probe.data}'
        result = result.strip()
        return result

    def reverse(self):
        probe = self.tail
        result = ''
        while probe.previous != self.tail:
            result += f'{probe.data} '
            probe = probe.previous
        result += f'{probe.data}'
        result = result.strip()
        return result

    def str_by_steps(self, steps, direction='forward'):
        result = ''

        if direction == 'forward':
            probe = self.head
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.next
                steps -= 1

        if direction == 'backward':
            probe = self.tail
            while steps > 0:
                result += f'{probe.data} '
                probe = probe.previous
                steps -= 1

        result = result.strip()
        return result

    def search(self, target_item):
        # * Busqueda de un elemento
        probe = self.head
        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            print(f'Target item {target_item} has been found')
            return probe
        else:
            print(f'Target item {target_item} is not in the linked list')
            return -1

    def replace(self, target_item, new_item):
        # * Remplazo de un elemento
        probe = self.head

        while probe.next != self.head and target_item != probe.data:
            probe = probe.next

        if probe.data == target_item:
            probe.data = new_item
            print(
                f"{new_item} replace the old value {target_item}")
        else:
            print(f"The target item {target_item} is not in the linked list")

    def unshift(self, new_item):
        # * Insertar un nuevo elemento/nodo al inicio(head)
        if self.size == 0:
            self.head.data = new_item
        else:
            self.head = TwoWayNode(new_item, previous=self.tail, next=self.head)
            self.head.next.previous = self.head
            self.tail.next = self.head
        self.size += 1

    def append(self, new_item):
        # * Insertar un nuevo elemento/nodo al final(tail)
        if self.size == 0:
            self.tail.data = new_item
        else:
            self.tail = TwoWayNode(new_item, previous=self.tail, next=self.head)
            self.tail.previous.next = self.tail
            self.head.previous = self.tail
        self.size += 1

    def shift(self):
        # * Eliminar un elmento/nodo al inicio(head)
        if self.size == 0:
            return None

        removed_item = self.head.data
        self.head = self.head.next

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def pop(self):
        # * Eliminar un elmento/nodo al final(tail)
        if self.size == 0:
            return None

        removed_item = self.tail.data
        self.tail = self.tail.previous

        self.head.previous = self.tail
        self.tail.next = self.head

        self.size -= 1

        print(f'Removed_item: {removed_item}')
        return removed_item

    def insert(self, new_item, index):
        # * Agregar un nuevo elemento/nodo por "indice" (Cuenta de Head - Tail)
        if self.size == 0:
            self.head.data = new_item
            self.size += 1
        elif index <= 0:
            self.unshift(new_item)
        elif index >= self.size - 1:
            self.append(new_item)
        else:
            probe = self.head
            while index > 1 and probe.next != self.head:
                probe = probe.next
                index -= 1
            probe.next = TwoWayNode(new_item, previous=probe, next=probe.next)
            probe.next.next.previous = probe.next
            self.size += 1

    def delete_by_index(self, index):
        # * Eliminar un nuevo elemento/nodo por "indice" (Cuenta de Head - Tail)
        if self.size == 0:
            return None
        if index <= 0:
            self.shift()
        elif index >= self.size - 1:
            self.pop()
        else:
            probe = self.head
            while index > 1 and probe.next.next != self.head:
                probe = probe.next
                index -= 1
            removed_item = probe.next.data
            probe.next = probe.next.next
            probe.next.previous = probe
            self.size -= 1

            print(f'Removed_item: {removed_item}')
            return removed_item

    def clear(self):
        self.__init__()
        
        
class Stack:
    '''
    Basados en arrays o en LinkedLists
    LIFO (Last In First Out)
    '''

    def __init__(self) -> None:
        self.top = None
        self.size = 0
        self.__current__ = None
    

    def __iter__(self):
        self.__current__ = self.top
        return self

    def __next__(self):
        if not self.__current__:
            raise StopIteration
        else:
            next_node = self.__current__
            self.__current__ = next_node.next
        return next_node

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        return_data = 'Empty stack'
        if self.top:
            return_data = self.top.data
            self.top = self.top.next
            self.size -= 1
        return return_data
    
    def add(self, stack2):
        if len(stack2) > 0:
            for node2 in stack2:
                self.push(node2.data)
        else:
            print(f'Parameter stack is empty')


    def __contains__(self, data):
        if self.size > 0:
            return_node = self.top
            while return_node and return_node.data != data:
                return_node = return_node.next
        return return_node

    def clear(self):
        self.size = 0
        self.top = None

    def peek(self):
        return_data = 'Empty stack'
        if self.top:
            return_data = self.top.data
        return return_data
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        node = self.top
        position = 1
        return_str = '(\r\n'
        while(node):
            return_str += f'\tPosition {position} - dato {node.data}'
            position += 1
            node = node.next
        return_str += '\r\n)'
        return return_str
    
class Queues():
    '''
    FIFO: First In First Out
    Rear: Ultimo elemento
    Front: Primer elemento
    '''