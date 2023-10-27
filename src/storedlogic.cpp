#include <bits/stdc++.h>
using namespace std;

class Instruction{
    public:
    char Name = ""[0];
    union Function{
        template<typename T>
        constexpr void (*)();
    };
};

class Stack{
    vector<Instruction> CurrentStack;
};



int main(){
    Instruction Add;
    
    Add.Function = (*[](int x, int y){return x + y;});
    std::cout << Add.Function(2,3);

    return 0;
}