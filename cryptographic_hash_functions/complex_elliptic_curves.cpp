#include <iostream>

struct cp /*complex point */{
    long int r; //real component
    long int i; //imaginary component
    long int m; //modulo

    cp(int real, int imaginary){
        r = real;
        i = imaginary;
    };

    cp operator+(cp n){
        r = (r + n.r) % m;
        i = (i + n.i) % m;
        return *this;
    };

    cp operator-(cp n){
        r = (r - n.r) % m;
        i = (i - n.i) % m;
        return *this;
    };
};

int main(){
    cp a(1,2);
    cp b(3, -5);
    a = a - b;
    std::cout << a.i;
    return 0;
}