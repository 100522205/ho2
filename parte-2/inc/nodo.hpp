#ifndef NODO_HPP
#define NODO_HPP

#include <vector>

namespace nodo {
    class Nodo {
        public:
        int id;
        int g ;
        int f;
        Nodo* father;
        int cost;

        Nodo(int id, Nodo* father, int cost, 
            std::vector<int> children, int h): 
            id(id), father(father), cost(cost), c(children), h(h) {
                g = get_acc_cost();
                f = g + h;
            }
    
        bool operator==(const Nodo& other) const {
            return id == other.id;
        }

        private:
        std::vector<int> c;
        int h;

        int get_acc_cost() {
            if (father == nullptr) {
                return cost;
            } else {
                return cost + father->g;
            }
        };


};

} // namespace nodo


#endif // NODO_HPP

