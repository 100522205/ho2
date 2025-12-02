from grafo import Nodo
from abierta import Open_bfs
from cerrada import Closed_bfs

def dijks(start:Nodo, end:Nodo):
    open = Open_bfs(start)
    closed = Closed_bfs()

    while True:
        n = open.pop()
        if n == end:
            return n.g
        if not closed.contains(n):
            c = n.children()
            closed.add(n)
            for child in c:
                open.add(child)

    