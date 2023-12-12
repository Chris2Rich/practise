#include <bits/stdc++.h>
using namespace std;

struct task{
    public:
    vector<task*> requirements;
    bool completed = false;
    int id;

    task(){};

    task(int inp){id = inp;}
    
    task(int inp, vector<task*>* init){
        id = inp;
        requirements = *init;
    }
};

vector<task*> vectorizeworkload(vector<task*> graph){
    vector<task*> work(0);
    vector<task*> nowork(0);
    for(int i = 0; i < graph.size(); i++){
        if(graph[i]->requirements.size() == 0){
            nowork.push_back(graph[i]);
        }
    }

    int count = 5;

    while(count > 0){
        task* n = nowork[nowork.size()-1];
        nowork.pop_back();
        work.push_back(n);
        for(int i = 0; i < graph.size(); i++){
            for(int j = 0; j < graph[i]->requirements.size(); j++){
                if(graph[i]->requirements[j] == n){
                    graph[i]->requirements.erase(graph[i]->requirements.begin() + j);
                }
            }
            if(graph[i]->requirements.size() == 0){
                nowork.push_back(graph[i]);
            }
        }

        count--;
    }

    return work;
}

int main(){

    task task1(1);
    task task2(2);
    task task3(3);
    task task4(4);
    task task5(5);
    task task6(6);
    task task7(7);
    task task8(8);
    task task9(9);

    task1.requirements = {&task2, &task3};
    task2.requirements = {&task4};
    task3.requirements = {&task4, &task5};
    task4.requirements = {&task6, &task7};
    task5.requirements = {&task8};
    task6.requirements = {};
    task7.requirements = {&task9};
    task8.requirements = {&task9};

    auto workload = vectorizeworkload({&task1,&task2,&task3,&task4,&task5,&task6,&task7,&task8,&task9});

    for(task* x: workload){
        cout << x->id;
    }

    return 0;
}