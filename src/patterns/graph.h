#include "MArray.h"

struct Node;
struct Edge;


struct Edge{
    Node* Start;
    Node* End;
    double Weight = 1;

    Edge(){}

    Edge(double inp){
        Weight = inp;
    }

    Edge(Node* inp1, Node* inp2){
        Start = inp1;
        End = inp2;
    }

    Edge(Node* inp1, Node* inp2, double inp3){
        Start = inp1;
        End = inp2;
        Weight = inp3;
    }
};

struct Node{
    MArray<Edge> EdgeArray;
    double Value = 0;

    Node(){};

    Node(double inp){
        Value = inp;
    }

    Edge* Max(){
        double max = -__DBL_MAX__;
        Edge* ref = nullptr;
        for(int i = 0; i < EdgeArray.getsize(); i++){
            if(EdgeArray[i]->Weight > max){
                max = EdgeArray[i]->Weight;
                ref = EdgeArray[i];
            }
        }

        return ref;
    }

    Edge* Min(){
        double max = __DBL_MAX__;
        Edge* ref = nullptr;
        for(int i = 0; i < EdgeArray.getsize(); i++){
            if(EdgeArray[i]->Weight < max){
                max = EdgeArray[i]->Weight;
                ref = EdgeArray[i];
            }
        }

        return ref;
    }
};

struct ListNode{
    ListNode* Previous;
    ListNode* Next;
    double Val;
};

struct Graph{
    MArray<Node> NodeArray;

    Node* Find(double inp){
        for(int i = 0; i < NodeArray.getsize(); i++){
            if(NodeArray[i]->Value == inp){
                return NodeArray[i];
            }
        }
        return nullptr;
    }

    void Connect(Node* A, Node* B){
        Edge Connector = *new Edge(A,B);
        A->EdgeArray.append(&Connector);
        B->EdgeArray.append(&Connector);
    }

    void Connect(Node* A, Node* B, double val){
        Edge Connector = *new Edge(A,B, val);
        A->EdgeArray.append(&Connector);
        B->EdgeArray.append(&Connector);
    }

};

struct Tree{

};

struct List{
    ListNode* Start;
    size_t Length;
};