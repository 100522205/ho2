from grafo import Nodo, Graph
from abierta import Open_bfs
from cerrada import Closed_bfs

def dijks(grafo:Graph, start_id:int, end_id:int)->int | Nodo:
    start = grafo.gen_node(start_id)

    open = Open_bfs(start)
    closed = Closed_bfs()

    while True:
        n = open.pop()
        if n.id == end_id:
            return n.g, n
        if not closed.contains(n):
            children = grafo.expand_node(n)
            closed.add(n)
            for child in children:
                open.add(child)

    