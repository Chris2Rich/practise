#include <bits/stdc++.h>
using namespace std;

double fibonnaci(double n){
    
    struct{
        unordered_map<double,double> memo;

        double lambda(double n){
            if(n <= 2){
                return 1;
            }
            if(memo.find(n-1) == memo.end() || memo.find(n-2) == memo.end()){
                memo.insert({n-1,lambda(n-1)});
                memo.insert({n-2,lambda(n-2)});
                return lambda(n-1) + lambda(n-2);
            }
            return memo[n-1] + memo[n-2];
        }
    }func;

    return func.lambda(n);
}

string longestsubstring(string s){
    double maxval = 0;
    pair<double,double> maxgroup;
    for(pair<double,double> ptr = {0,1}; &s[ptr.second] < &s[s.size()];){
        if(s[ptr.first] == s[ptr.second]){
            ptr.second++;
            if(maxval < ptr.second-ptr.first){
                maxgroup.first = ptr.first;
                maxgroup.second = ptr.second;
            }
            maxval = max(maxval, ptr.second-ptr.first);
        }
        else{
            ptr.first++;
        }
    }
    return s.substr(maxgroup.first,maxgroup.second);
}

int main(){

    int testsize = 8;

    time_t now = time(&now);
    srand(now);
    clock_t start, end;
    start = clock();
    std::ios_base::sync_with_stdio(false);

    auto ans = longestsubstring("AAABCDEEEEE");

    end = clock();

    double total_time = (end - start) / (float)CLOCKS_PER_SEC;
    std::cout << "Elapsed Time : " << total_time << "s\n";
    std::cout << ans;

    return 0;
}