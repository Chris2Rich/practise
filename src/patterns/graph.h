#include <vector>
#include <iostream>

class graph{
    public:
    std::vector<std::vector<double>> adjacency_matrix;

    graph(double n){
        for(int i = 0; i < n; i++){
            adjacency_matrix.push_back(std::vector<double>(n,0));
        }
    }
};
