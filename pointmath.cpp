#include <iostream>
#include <x86intrin.h>

#define int64 long long int
#define int32 long int

// #define int64 short int
// #define int32 signed char 

#define s64 sizeof(int64) * 8
#define s32 sizeof(int32) * 8

struct point{
    private:
    int64 val;

    public:

    point(){
        val = 0;
    }

    point(int32 x, int32 y){
        val = ((x << s32) + y);
    }

    inline int32 x(){
        return (val >> s32);
    }

    inline int32 y(){
        return ((val << s32) >> s64);
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
    point a(1,6);
    
    //std::cout << a.x();
    return 0;
}