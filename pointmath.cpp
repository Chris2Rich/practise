#include <iostream>
#include <x86intrin.h>

#define int64 long long int
#define int32 long int

// #define int64 short int
// #define int32 signed char 

#define s64 sizeof(int64) * 8
#define s32 sizeof(int32) * 8

struct point{
    inline static int64 create(int32 x, int32 y){
        return ((x << s32) + y);
    }

    static inline int32 x(int64 n){
        std::cout << (n >> s32);
        return (n >> s32);
    }

    static inline int32 y(int64 n){
        std::cout << ((n << s32) >> s64);
        return ((n << s32) >> s64);
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
    int64 a = point::create(1,2);
    point::x(a);
    return 0;
}
