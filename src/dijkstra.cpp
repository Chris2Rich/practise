#include "patterns\graph.h"

int main(){

    int testsize = 3;

    time_t now = time(&now);
    srand(now);
    clock_t start, end;
    start = clock();
    std::ios_base::sync_with_stdio(false);

    Graph TestGraph;
    TestGraph.NodeArray.append(new Node(rand()));

    for(int i = 1; i < testsize; i++){
        TestGraph.NodeArray.append(new Node(rand()));
        TestGraph.Connect(TestGraph.NodeArray[std::min(testsize-1,rand())], TestGraph.NodeArray[std::min(testsize-1,rand())], rand());
    }

    auto Ans = TestGraph.NodeArray[0]->MaxEdge()->Weight;;

    end = clock();

    float total_time = float(end-start) / float(CLOCKS_PER_SEC);
    std::cout << "Time taken for function : " << total_time << " secs\n";
    std::cout << Ans;

    return 0;
}