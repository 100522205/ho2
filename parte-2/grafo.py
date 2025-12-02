from grafo import Nodo

class Graph():
    def __init__(self, vertices:list, arcos:list):
        """
        
        :param vertices: [id1, id2, ...]
        :param arcos: [(id1, id2, cost12), ...]
        """
        self.v = vertices
        self.a = arcos
        self.cost = {(i, j): cost for (i, j, cost) in arcos}
        self.adj = {i: [] for i in range(vertices)+1}
        for (i, j) in arcos:
            self.adj[i].append(j)



class Nodo():
    def __init__(self, id:int, father:Nodo, cost:int, children: list):
        self.id = id
        self.father = father
        self.cost = cost
        self.g = father.g + self.cost
        self.c = children

        def children(self)->list:
            return self.c

def parse_coords(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    v = []
    
    for line in lines:
        if line.startswith('v'):
            v.append(int(line.split()[1]))

    return v

def parse_arcs(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    a = []
    
    for line in lines:
        if line.startswith('a'):
            parts = line.split()
            a.append((int(parts[1]), int(parts[2]), int(parts[3])))

    return a

print(int("v 1 -121745853 37608914".split()[1]))