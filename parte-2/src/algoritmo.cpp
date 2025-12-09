#include "algoritmo.hpp"
#include "grafo.hpp"
#include "nodo.hpp"
#include "abierta.hpp"
#include "cerrada.hpp"

#include <tuple>

std::tuple<int, nodo::Nodo*>algoritmo::dijks(grafo::Grafo& g, int start_id, int end_id) {
    nodo::Nodo* n = g.gen_node(start_id, end_id);

    abierta::Open open = abierta::Open(*n);
    cerrada::Closed closed = cerrada::Closed();
    

    while (true) {
        n = open.pop();
        if (n->id == end_id) {
            return {n->g, n};
        }
        if (not closed.contains(*n)) {
            std::vector<nodo::Nodo*> children = g.expand_node(n, end_id);
            closed.add(*n);
            for (auto& child : children) {
                open.add_nh(*child);
            }
        }
    }

}

std::tuple<int, nodo::Nodo*> algoritmo::a_star(grafo::Grafo& g, int start_id, int end_id) {
    nodo::Nodo* n = g.gen_node(start_id, end_id);
    
    abierta::Open open(*n);
    cerrada::Closed closed;
    
    while (true) {
        n = open.pop();
        if (n->id == end_id) {
            return {n->g, n};
        }
        if (!closed.contains(*n)) {
            std::vector<nodo::Nodo*> children = g.expand_node(n, end_id);
            closed.add(*n);
            for (auto& child : children) {
                open.add_h(*child); 
            }
        }
    }
}