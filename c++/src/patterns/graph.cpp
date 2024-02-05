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

    double insert(std::vector<double> weights){
        
    }

    void print(){
        for(int i = 0; i < adjacency_matrix.size(); i++){
            for(int j = 0; j < adjacency_matrix.size(); j++){
                std::cout << "| " << adjacency_matrix[i][j] << " |";
            }
            std::cout << "\n";
        }
    }
};

int main(){

    graph newgraph(6);
    newgraph.adjacency_matrix[0][0] = 15;
    newgraph.print();

    return 0;
}