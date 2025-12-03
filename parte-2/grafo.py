from typing import Self

class Nodo():
    def __init__(self, id:int, father:Self, cost:int, children: list):
        self.id = id
        self.father = father
        self.cost = cost
        self.g = father.g + self.cost if father else self.cost
        self.c = children # [id, ...]

    def __lt__(self, other:Self)->bool:
        return self.g < other.g

    def __eq__(self, other:Self)->bool:
        return self.id == other.id

    def children(self)->list:
        return self.c


class Graph():
    def __init__(self, vertices:list, arcos:list):
        """
        
        :param vertices: [id1, id2, ...]
        :param arcos: [(id1, id2, cost12), ...]
        """
        self.v = vertices
        self.proc_v = len(vertices)
        self.a = arcos
        self.proc_a = len(arcos)
        self.exp = 0
        self.cost = {(i, j): cost for (i, j, cost) in arcos}
        self.adj = {i: [] for i in vertices}
        for (i, j) in self.cost:
            self.adj[i].append(j)

    def gen_node(self, id:int, father:Nodo=None)->Nodo:
        children = []
        for j in self.adj[id]:
            child = j
            children.append(child)
        return Nodo(id, father, 0 if father is None else self.cost[(father.id, id)], children)
    
    def expand_node(self, node:Nodo)->list:
        self.exp += 1
        children = []
        for child in node.children():
            child_id = child
            children.append(self.gen_node(child_id, node)) 
        return children


