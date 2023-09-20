#include <iostream>

class OperateVal{
private:
    float val;
    struct ReturnVal{
        float vals[4];
        ReturnVal(float inpa, float inpb, float inpc, float inpd){
            vals[0] = inpa;
            vals[1] = inpb;
            vals[2] = inpc;
            vals[3] = inpd;
            
        float operator[](int i){
            return (i < 4) ? vals[i] : 0;
            }
        }
    };
public:

    OperateVal(float inp){
        val = inp;
    }

    ReturnVal operator()(float inp){
        ReturnVal ans(inp+val, inp-val, inp*val, inp/val);
        return ans;
    }
};

class Map{
    template <typename T>
    Map(T inp){
        return Map<inp>;
    }
};

int main(){
    auto fn = OperateVal(2);
    std::cout << fn(5)[2];
    return 0;
}