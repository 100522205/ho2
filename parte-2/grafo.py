from typing import Self

class Nodo():
    def __init__(self, id:int, father:Self, cost:int, children: list, h:int):
        self.id = id
        self.father = father
        self.cost = cost
        self.g = father.g + self.cost if father else self.cost
        self.h = h
        self.f = self.g + self.h
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
        
        :param vertices: [(id1, lat1, lon1), (id2, lat2, lon2), ...]
        :param arcos: [(id1, id2, cost12), ...]
        """
        self.v = vertices
        self.proc_v = len(vertices)
        self.a = arcos
        self.proc_a = len(arcos)
        self.exp = 0
        self.cost = {(i, j): cost for (i, j, cost) in arcos}
        self.adj = {i: [] for (i, _, _) in vertices}
        for (i, j) in self.cost:
            self.adj[i].append(j)

    def manhattan(self, id:int, end_id:int)->int:
        lat1, lon1 = self.v[id][1], self.v[id][2]
        lat2, lon2 = self.v[end_id][1], self.v[end_id][2]
        return abs(lat1 - lat2) + abs(lon1 - lon2)

    def gen_node(self, id:int, end_id:int, father:Nodo=None)->Nodo:
        children = []
        for j in self.adj[id]:
            child = j
            children.append(child)
        return Nodo(id, father, 0 if father is None else self.cost[(father.id, id)], children, self.manhattan(id, end_id))    
    
    def expand_node(self, node:Nodo, end_id:int)->list:
        self.exp += 1
        children = []
        for child in node.children():
            child_id = child
            children.append(self.gen_node(child_id, end_id, node)) 
        return children


