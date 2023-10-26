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
    int (*a)(int,int) = [](int x, int y){return x + y;};
    Add.Function = reinterpret_cast<void (*)(void)> (a);
    auto f = reinterpret_cast<int (*)(int,int)> (Add.Function);
    std::cout << f(2,3);

    return 0;
}