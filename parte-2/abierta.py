from grafo import Nodo


class Open_bfs():
    def __init__(self, max_dist: int, start: Nodo):
        self.nodes = [[] for _ in range(max_dist+1)]
        self.nodes[max_dist].append(start)
        self.max_dist = max_dist
        self.min = max_dist
    
    def __str__(self):
        out = ""
        for i in range(len(self.nodes)):
            if len(self.nodes[i]) > 0:
                out += f"{i}: {[(node.id, node.g, node.h, node.f) for node in self.nodes[i]]}\n"
        return out
    
    def add_nh(self, node: Nodo):
        self.nodes[node.g].append(node)
        if node.g < self.min:
            self.min = node.g

    def add_h(self, node: Nodo):
        self.nodes[node.f].append(node)
        if node.f < self.min:
            self.min = node.f

    def is_empty(self, n: int):
        if len(self.nodes[n]) > 0:
            return False
        return True

    def search_min(self):
        for i in range(self.min, len(self.nodes)):
            if not self.is_empty(i):
                self.min = i
                return
        self.min = self.max_dist
    
    def pop(self):
        node = self.nodes[self.min][-1]
        del self.nodes[self.min][-1]
        if self.is_empty(self.min):
            self.search_min()
        return node


