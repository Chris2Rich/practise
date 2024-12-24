// Part 1
#include <iostream>
#include <vector>
#include <math.h>

// --- Question 1

// constexpr double fibonnacci(double n){
//     return (pow(((1 + sqrt(5)) / 2), n) - pow(((1 - sqrt(5)) / 2), n)) / sqrt(5);
// }

// --- Question 1: a

// std::vector<double> zeckendorf(double n){
//     std::vector<double> ans = {};
//     for(double ptr = n; ptr > 0; ptr--){
//         if(n >= fibonnacci(ptr)){
//             ans.push_back(fibonnacci(ptr));
//             n -= fibonnacci(ptr);
//         }
//     }

//     return ans;
// }

// int main(int argc, char** argv){
//     std::vector<double> test = zeckendorf(1000);
//     for(auto x: test){
//         std::cout << x << " ";
//     }
//     return 0;
// }

// --- Question 1: b

//832040

// --- Question 1: c

// double zeckendorf(double n){
//     double ans = 0;
//     for(double ptr = n; ptr > 0; ptr--){
//         if(n >= fibonnacci(ptr)){
//             ans++;
//             n -= fibonnacci(ptr);
//         }
//     }

//     return ans;
// }

// int main(int argc, char** argv){
//     double n = 0;
//     for(int i = 0; i < 53316291; i++){
//         if(zeckendorf(i) == 3){
//             n++;
//         }
//     }

//     std::cout << "\n" << n;
    
//     return 0;
// }

// --- Question 1: d

// double zeckendorf(double n){
//     for(double ptr = n; ptr > 0; ptr--){
//         if(n >= fibonnacci(ptr)){
//             n -= fibonnacci(ptr);
//             if(fibonnacci(ptr) == 701408733){
//                 return false;
//             }
//         }
//     }

//     return true;
// }

// int main(int argc, char** argv){
//     double n = 0;
//     for(int i = 1000000000; i < 5000000000; i++){
//         if(zeckendorf(i)){
//             n++;
//         }
//     }

//     std::cout << "\n" << n;
    
//     return 0;
// }