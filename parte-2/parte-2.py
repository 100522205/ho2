#!/usr/bin/env python3

from grafo import Nodo, Graph
from algoritmo import dijks, a_star
import sys
import time
from format_time import format_time
from parser import parse_coords, parse_arcs


def main():
    if len(sys.argv) != 5:
        print("Usage: ./parte-2.py <start_id> <end_id> <directory> <ouput>")
        sys.exit(1)

    start_id = int(sys.argv[1])
    end_id = int(sys.argv[2])
    directory = sys.argv[3]
    output = sys.argv[4]

    if directory.endswith('/'):
        opendir = directory
        directory = directory[:-1]
    else:
        opendir = directory + '/'

    vertices = parse_coords(opendir + f"{directory}.co")
    arcs = parse_arcs(opendir + f"{directory}.gr")

    grafo = Graph(vertices, arcs)

    inicio = time.time()
    cost, end = a_star(grafo, start_id, end_id)
    fin = time.time()
    
    time_elapsed = fin - inicio
    ratio = grafo.exp / time_elapsed
    time_elapsed = format_time(time_elapsed)
    ratio = format_time(ratio)

    print("\n")
    print(f"#vertices: {grafo.proc_v}")
    print(f"#arcos   : {grafo.proc_a}")
    print(f"Solución óptima encontrada con coste {cost}")
    print("\n")
    print(f"Tiempo de ejecución: {time_elapsed} segundos")
    print(f"expansiones        : {grafo.exp} ({ratio} nodes/sec)")

    with open(output, 'w') as f:
        path = [end]
        node = end
        for i in range(grafo.exp+1):
            if node.father is None:
                break
            path.append(node.father)
            node = node.father
        path.reverse()

        out = ""

        for i in range(len(path)):
            if i == 0:
                out += f"{path[i].id} "
            else:
                out += f"- ({path[i].cost}) - {path[i].id} "

        f.write(out)


if __name__ == "__main__":
    main()