#include <iostream>

struct cp /*complex point */{
    long int r; //real component
    long int i; //imaginary component
    long int m; //modulo

    cp(int real, int imaginary){
        r = real;
        i = imaginary;
    }

    cp operator+(cp n){
        r = (r + n.r) % m;
        i = (i + n.i) % m;
    }

    cp operator-(cp n){
        r = (r - n.r) % m;
        i = (i - n.i) % m;
    }
}

int main(){

    return 0;
}