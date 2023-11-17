#include <vector>
#include <iostream>

class Graph{
    public:
    std::vector<std::vector<double>> AdjacencyMatrix;

    Graph(double n){
        for(int i = 0; i < n; i++){
            AdjacencyMatrix.push_back(std::vector<double>(n,0));
        }
    }
};
