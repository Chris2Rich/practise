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
    vector<task*> workload(0);
    queue<task*> q;
    graph[0]->completed = true;
    q.push(graph[0]);
    while(!q.empty()){
      task* v = q.front();
      q.pop();
      v->completed = true;
      workload.push_back(v);
      for(int i = 0; i < v->requirements.size(); i++){
        q.push(v->requirements[i]);
      }
    }
    
    reverse(workload.begin(), workload.end());
    return workload;
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
