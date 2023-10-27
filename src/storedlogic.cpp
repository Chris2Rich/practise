#include <bits/stdc++.h>
using namespace std;

class Instruction{
    public:
    char Name = ""[0];
    void (*Function)(void);
};

class Stack{
    vector<Instruction> CurrentStack;
};



int main(){
    Instruction Add;
    
    Add.Function = reinterpret_cast<void (*)(void)> (*[](int x, int y){return x + y;});
    auto f = reinterpret_cast<int (*)(int,int)> (Add.Function);
    std::cout << f(2,3);

    return 0;
}