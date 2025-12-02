from grafo import Nodo

class Closed_bfs():
    def __init__(self):
        self.nodes = set()

    def add(self, node:Nodo):
        self.nodes.add(node.id)

    def contains(self, node:Nodo)->bool:
        return node.id in self.nodes