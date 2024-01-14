#include <iostream>
#include <x86intrin.h>

#define int64 long long int
#define int32 long int

// #define int64 short int
// #define int32 signed char 

#define s64 sizeof(int64)
#define s32 sizeof(int32)

struct point{

    inline static int64 create(int32 x, int32 y){
        return ((x << s32) + y);
    }

    inline static int32 x(int64 val){
        return (val >> s32);
    }

    inline static int32 y(int64 val){
        return val;
    }
};

void bin(int64 x){
    for(int64 i = s64; i >= 0; i--){
        std::cout << ((x >> i) & 1);
    }
    std::cout << '\n';
}

void bin(int32 x){
    for(int32 i = s32; i >= 0; i--){
        std::cout << ((x >> i) & 1);
    }
    std::cout << '\n';
}

int main(){
    int64 pointa = point::create(1,6);
    bin(pointa);
    std::cout << (int64) point::y(pointa);
    return 0;
}