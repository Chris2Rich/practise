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
    int maxval = 0;
    pair<int,int> maxgroup;
    for(pair<int,int> ptr = {0,1}; &s[ptr.second] < &s[s.size()];){
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

char modechar(string s){
    unordered_map<char,int> memo;
    int maxval = 0;
    char maxchar = 0;
    for(int c = 0; c <= 127; c++){
        memo.insert({(char)c,0});
    }
    for(int i = 0; i < s.size(); i++){
        memo[s[i]]++;
    }
    for(auto x : memo){
        if(maxval < x.second){
            maxchar = x.first;
        }
        maxval = max(maxval, x.second);
    }
    return maxchar;
}

int maxsubarr(vector<int> v, int n){
    int s = 0;
    int e = n;
    int maxval = INT_MIN;
    while(e <= v.size()){
        maxval = max(maxval, accumulate(v.begin()+s,v.begin()+e,0));
        s++;
        e++;
    }
    return maxval;
}

int maxsubseq(vector<int> v, int n){
    int p = 0;
}

int main(){

    int testsize = 8;

    time_t now = time(&now);
    srand(now);
    clock_t start, end;
    start = clock();
    std::ios_base::sync_with_stdio(false);

    auto ans = maxsubarr({3,6,5,1,2,2,3,6,15,9},4);

    end = clock();

    double total_time = (end - start) / (float)CLOCKS_PER_SEC;
    std::cout << "Elapsed Time : " << total_time << "s\n";
    std::cout << ans;

    return 0;
}