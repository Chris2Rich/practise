#include <bits/stdc++.h>
using namespace std;

class node{
    int val;
    vector<node*> nodearray;
    function<int(int)> func = function<int(int)>([&](int x){return x + val;});

    node(int inp){
        val = inp;
    }
};

class graph{
    node* root;
    unordered_map<node*, bool> memo;
};

vector<node> vectorisegraph(graph g){

}

int main(){

    return 0;
}