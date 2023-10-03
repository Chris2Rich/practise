#include "MArray.h"

struct Node{};
struct ListNode{};

struct Edge{};
struct Graph{};
struct Tree{};
struct List{};

struct Node{
    MArray<Edge> EdgeArray();
    double Value = 0;
};

struct ListNode{
    ListNode* Previous;
    ListNode* Next;
    double val;
};

struct Edge{
    Node* Start;
    Node* End;
    double Weight = 0;
};

struct Graph{
    MArray<Node> NodeArray();
};

struct Tree{

};

struct List{
    ListNode* Start;
    size_t Length;
};