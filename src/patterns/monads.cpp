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
    
    void resize(int inpsize){
        T* Temp = new T[inpsize];
        for(int i = 0; i < std::min(size,inpsize); i++){
            Temp[i] = Array[i];
        }
        
        size = inpsize;
        Array = Temp;
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

struct{
    static float Halve(float inp){
        return inp/2.0;
    }
} Functions;

int main(int argc, char* argv[]){

    time_t now = time(&now);
    srand(now);

    auto fn = 1;
    List<float> ElementList(5);
    ElementList.randfill();
    ElementList.map(Functions.Halve);
    ElementList.resize(8);

    ElementList.print();
    return 0;
}