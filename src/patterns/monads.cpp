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

    T* operator[](int i){
        return &Array[i];
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
    
    void append(T inp){
        this->resize(size+1);
        Array[size-1] = inp;
    }
    
    T popback(){
        T ans = Array[size-1];
        this->resize(size-1);
        return ans;
    }
    
    T popfront(){
        T ans = Array[0];
        for(int i = 0; i < size-1; i++){
            Array[i] = Array[i+1];
        }
        this->resize(size-1);
        return ans;
    }
    
    bool searchlinear(T val){
        for(int i = 0; i < size; i++){
            if(Array[i] == val){
                return true;
            }
            if(Array[size-1-i] == val){
                return true;
            }
        }
        return false;
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
    
} Functions;

struct Pixel{
    int r = 0;
    int b = 0;
    int g = 0;
    
    Pixel operator+(Pixel inp){
        this->r += inp.r;
        this->b += inp.b;
        this->g += inp.g;
        return *this;
    }
};

int main(int argc, char* argv[]){

    time_t now = time(&now);
    srand(now);

    List<Pixel> ElementList(10);
    ElementList.randfill();
    return 0;
}