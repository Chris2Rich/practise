#include "patterns\graph.h"

int main(){

    Graph TestGraph;
    MArray<Node> Nodes = TestGraph.NodeArray;
    for(int i = 0; i < 5; i++){
        Nodes.append(new Node);
    }

    TestGraph.Connect(Nodes[0], Nodes[1]);
    TestGraph.Connect(Nodes[0], Nodes[2]);
    TestGraph.Connect(Nodes[0], Nodes[3]);
    TestGraph.Connect(Nodes[1], Nodes[2]);
    TestGraph.Connect(Nodes[1], Nodes[4]);
    TestGraph.Connect(Nodes[2], Nodes[3]);
    TestGraph.Connect(Nodes[2], Nodes[4]);
    TestGraph.Connect(Nodes[3], Nodes[4]);

    Edge* MaxEdge = Nodes[0]->Min();
    std::cout << MaxEdge->Weight;

    return 0;
}