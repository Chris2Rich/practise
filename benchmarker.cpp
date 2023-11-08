#include <bits/stdc++.h>

int main(int argc, char** argv){
    char* endptr;
    std::cout << std::strtod(argv[1], &endptr) + std::strtod(argv[2], &endptr);
    return 0;
}