#include <iostream>

class OperateVal{
private:
    float val;
public:

    OperateVal(float inp){
        val = inp;
    }

    float* operator()(float inp){
        float ans[4] = {inp+val, inp-val, inp*val, inp/val};
        return ans;
    }
};

void map(){
    
}

int main(){
    auto fn = OperateVal(2);
    std::cout << fn(5)[2];
    return 0;
}