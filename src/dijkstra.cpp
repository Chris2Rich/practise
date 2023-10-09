#include "patterns\graph.h"

int main(){

    int testsize = 5;

    time_t now = time(&now);
    srand(now);
    clock_t start, end;
    start = clock();
    std::ios_base::sync_with_stdio(false);

    Graph TestGraph;

    for(int i = 0; i <= testsize; i++){
        TestGraph.NodeArray.append(new Node(rand()));
        TestGraph.DConnect(TestGraph.NodeArray[std::min(TestGraph.NodeArray.getsize()-1,rand())], TestGraph.NodeArray[std::min(TestGraph.NodeArray.getsize()-1,rand())], rand());
    }

    end = clock();

    float total_time = float(end-start) / float(CLOCKS_PER_SEC);
    std::cout << "Time taken for function : " << total_time << " secs\n";
    TestGraph.Print();

    return 0;
}