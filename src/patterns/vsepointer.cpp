#include <iostream>

template <typename T>
class sve{
public:
    T* s;
    T* v;
    T* e;

    sve(T* start, T* value, T* end){
        s = start;
        v = value;
        e = end;
    }

    void operator++(int){
        v = 
        (T*) ((v+1 <= e) * (uintptr_t) (v+1) + (v+1 > e) * (uintptr_t) (s));
        //(next <= end) * (next) + (next > end) * (start) 
        ;
    }
    
    void operator--(int){
        (T*) ((v-1 >= s) * (uintptr_t) (v-1) + (v-1 < s) * (uintptr_t) (e));
        //(prev >= start) * (prev) + (prev < start) * (end)
    }

};

int main(){
    int arr[3] {1,2,3};
    sve ptr(&arr[0], &arr[1], &arr[2]);
    ptr--;

    std::cout << *ptr.v;
}