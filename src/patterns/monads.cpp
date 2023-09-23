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
    
    T* operator[](int i){
        return &Array[i];
    }
    
    void operator+=(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] += inp->Array[i];
        }
    }
    
    void operator-=(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] -= inp->Array[i];
        }
    }
    
    void operator*=(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] *= inp->Array[i];
        }
    }
    
    void operator/=(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] /= inp->Array[i];
        }
    }
    
    void operator%=(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] %= inp->Array[i];
        }
    }

    List<T>* operator+(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] += inp->Array[i];
        }
        return this*
    }

    List<T>* operator-(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] -= inp->Array[i];
        }
        return this*
    }

    List<T>* operator*(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] *= inp->Array[i];
        }
        return this*
    }

    List<T>* operator/(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] /= inp->Array[i];
        }
        return this*
    }

    List<T>* operator%(const List<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] %= inp->Array[i];
        }
        return this*
    }
    
    bool operator>(const List<T>* inp){
        for(int i = 0; i < std::min(size, inp->size); i++){
            if(Array[i] > inp->Array[i]){
                return true;
            }
        }
        if(size > inp->size){
            return true;
        }
        return false;
    }
    
    bool operator<(const List<T>* inp){
        for(int i = 0; i < std::min(size, inp->size); i++){
            if(Array[i] < inp->Array[i]){
                return true;
            }
        }
        if(size < inp->size){
            return true;
        }
        return false;
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

int main(int argc, char* argv[]){
    time_t now = time(&now);
    srand(now);
    return 0;
}