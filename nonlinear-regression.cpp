#include <math.h>
#include <iostream>
#include <vector>
#include <utility>

std::vector<double> LogReduce(std::vector<double>* a){
    std::vector<double> b;
    for(int i = 0; i < a->size(); i++){
        b[i] = log(a->operator[](i));
    }

    return b;
}

double Error(std::vector<std::vector<double>>* a, double (*func)(double)){
    double ans = 0;

    for(int i = 0; i < a->size(); i++){
    ans += pow((func(a->operator[](i)[0]) - a->operator[](i)[1]), 2);
    }

    return ans / (float) a->size();
}

double xy(double x){
    return x+2;
}

int main(){
    std::vector<std::vector<double>> data = {{1,2},{2,4},{3,5},{4,6},{5,7}};
    std::cout << Error(&data, &xy);
    return 0;
}