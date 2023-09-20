#include <iostream>
template <typename T>
class List{
private:
    T* Array;
    int size;

public:
    List(int inpsize){
        Array = new T[inpsize];
        size = inpsize;
    }

    T operator[](int i){
        return Array[i];
    }

    void fill(T Val){
        for(int i = 0;  i < size; i++){
            Array[i] = Val;
        }
    }

    void randfill(){
        for(int i = 0;  i < size; i++){
            Array[i] = rand();
        }
    }

    void map(T(func)(T)){
        for(int i = 0; i < size; i++){
            Array[i] = func(Array[i]);
        }
    }

    void print(){
        for(int i = 0; i < size; i++){
            std::cout << Array[i] << " ";
        }
    }
};

struct{
    static int EvenFilter(int inp){
        return inp * (inp % 2 == 0);
    }

    static int OddFilter(int inp){
        return inp * (inp % 2 != 0);
    }
} Filters;

int main(int argc, char* argv[]){

    time_t now = time(&now);
    srand(now);

    auto fn = 1;
    List<int> ElementList(5);
    ElementList.randfill();
    ElementList.map(Filters.EvenFilter);

    ElementList.print();
    return 0;
}