#include <iostream>
#include <bitset>
#include <vector>
#include <cstdint>
using namespace std;

#define size_d (sizeof(double) * 8)

constexpr bitset<size_d> conv_dtb(const double n){
    bitset<size_d> res;
    uint64_t m = n;
    for(int i = 0; i < size_d; i++){
        res.set(i, ((m >> i) & 1));
    }
    return res;
}

int main(){
    double a = 234723764623;
    cout <<  conv_dtb(a);
    return 0;
}