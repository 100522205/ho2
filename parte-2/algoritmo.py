from grafo import Nodo, Graph
from abierta import Open_bfs
from cerrada import Closed_bfs

def dijks(grafo:Graph, start_id:int, end_id:int)-> tuple[int, Nodo]:
    n = grafo.gen_node(start_id, end_id)

    open = Open_bfs(1000000, n)
    closed = Closed_bfs()


    while True:
        print( open )
        n = open.pop()
        if n.id == end_id:
            return n.g, n
        if not closed.contains(n):
            children = grafo.expand_node(n, end_id)
            closed.add(n)
            for child in children:
                open.add_nh(child)


def a_star(grafo:Graph, star_id:int, end_id:int)-> tuple[int, Nodo]:
    n = grafo.gen_node(star_id, end_id)

    open = Open_bfs(1000000, n)
    closed = Closed_bfs()

    while True:
        n = open.pop()
        if n.id == end_id:
            return n.g, n
        if not closed.contains(n):
            children = grafo.expand_node(n, end_id)
            closed.add(n)
            for child in children:
                open.add_h(child)