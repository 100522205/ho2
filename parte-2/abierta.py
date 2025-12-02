import heapq

class Open_bfs():
    def __init__(self, start):
        self.nodes = [start]
    
    def add(self, node):
        heapq.heappush(self.nodes, node)

    def pop(self):
        return heapq.heappop(self.nodes)