#include <bits/stdc++.h>

int main(int argc, char* argv[], char* envp[]){
        for(int i = 1; i < argc; i++){
            std::cout << argv[i] << "x^" << argc - i - 1 << "\n";
        }
    return 0;
}