#include "patterns\graph.h"

int main(){

    int testsize = 1000;

    time_t now = time(&now);
    srand(now);
    clock_t start, end;
    start = clock();
    std::ios_base::sync_with_stdio(false);

    Graph TestGraph;
    TestGraph.NodeArray.append(new Node(rand()));

    for(int i = 1; i <= testsize; i++){
        TestGraph.NodeArray.append(new Node(rand()));
        TestGraph.DConnect(TestGraph.NodeArray[i], TestGraph.NodeArray[i-1], rand());
    }

    end = clock();

    double total_time = end- start / (float)CLOCKS_PER_SEC;
    std::cout << "Elapsed Time : " << total_time << "s\n";
    TestGraph.Print();

    return 0;
}