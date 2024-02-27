#include <math.h>
#include <iostream>
#include <vector>
#include <climits>

typedef double (*lfunc)(double);

std::vector<double> LogReduce(std::vector<double>* a){
    std::vector<double> b;
    for(int i = 0; i < a->size(); i++){
        b[i] = log(a->operator[](i));
    }

    return b;
}

double MSE(std::vector<std::vector<double>>* a, double (*func)(double)){
    double ans = 0;

    for(int i = 0; i < a->size(); i++){
    ans += pow((func(a->operator[](i)[0]) - a->operator[](i)[1]), 2);
    }

    return ans / (float) a->size();
}

double MAE(std::vector<std::vector<double>>* a, double (*func)(double)){
    double ans = 0;

    for(int i = 0; i < a->size(); i++){
    ans += abs((func(a->operator[](i)[0]) - a->operator[](i)[1]));
    }

    return ans / (float) a->size();
}

double lambda(double x, double m, double c){
    return ((m*x) + c);
}

lfunc SGD(std::vector<std::vector<double>>* a, double tolerance){
    double prev = LLONG_MAX;
    double m = 0;
    double c = 0;
}

int main(){
    std::vector<std::vector<double>> data = {{1,2},{2,17},{3,5},{4,6},{5,7}};
    return 0;
}
