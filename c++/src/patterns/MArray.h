#include <iostream>
#include<math.h>

template <typename T>
class MArray{
private:

    T* Array;
    int size;

public:
    
    int getsize(){
        return size;
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
    
    void append(T* inp){
        this->resize(size+1);
        Array[size-1] = *inp;
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
    
    bool searchlinear(const T val){
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

    void Sort(){
        
    }

    void map(T(func)(T)){
        for(int i = 0; i < size; i++){
            Array[i] = func(Array[i]);
        }
    }

    void map(T(func)(T,int)){
        for(int i = 0; i < size; i++){
            Array[i] = func(Array[i],i);
        }
    }

    MArray<MArray<T>> map(MArray<T>(func)(T)){
        MArray<MArray<T>> ans = *new MArray<MArray<T>>(size);
        for(int i = 0; i < size; i++){
            *ans[i] = func(Array[i]);
        }
        return ans;
    }

    MArray<MArray<T>> map(MArray<T>(func)(T,int)){
        MArray<MArray<T>> ans = *new MArray<MArray<T>>(size);
        for(int i = 0; i < size; i++){
            *ans[i] = func(Array[i],i);
        }
        return ans;
    }

    T flatten(){
        T ans(0);
        for(int i = 0; i < size; i++){
            for(int j = 0; j < Array[i].getsize(); j++){
                ans.append(Array[i].operator[](j));
            }
        }
        return ans;
    }

    void print(){
        for(int i = 0; i < size; i++){
            std::cout << Array[i] << " ";
        }
    }
    
    T* operator[](const int i){
        return &Array[i];
    }
    
    void operator+=(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] += inp->Array[i];
        }
    }
    
    void operator-=(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] -= inp->Array[i];
        }
    }
    
    void operator*=(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] *= inp->Array[i];
        }
    }
    
    void operator/=(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] /= inp->Array[i];
        }
    }
    
    void operator%=(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] %= inp->Array[i];
        }
    }

    MArray<T>* operator+(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] += inp->Array[i];
        }
        return this;
    }

    MArray<T>* operator-(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] -= inp->Array[i];
        }
        return this;
    }

    MArray<T>* operator*(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] *= inp->Array[i];
        }
        return this;
    }

    MArray<T>* operator/(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] /= inp->Array[i];
        }
        return this;
    }

    MArray<T>* operator%(const MArray<T>* inp){
        if(inp->size > size){
            this->resize(inp->size);
        }
        
        for(int i = 0; i < size; i++){
            Array[i] %= inp->Array[i];
        }
        return this;
    }
    
    bool operator>(const MArray<T>* inp){
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
    
    bool operator<(const MArray<T>* inp){
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

    bool operator==(const MArray<T>* inp){
        for(int i = 0; i < std::min(size, inp->size); i++){
            if(Array[i] == inp->Array[i]){
                return true;
            }
        }

        if(size == inp->size){
            return true;
        }
        return false;
    }

    void* operator new(size_t inpsize){
        void* ptr = malloc(inpsize);
        return ptr;
    }

    void operator delete(void* ptr){
        free(ptr);
    }

    MArray<T>(){
        Array = new T[0];
        size = 0;
    }

    MArray<T>(size_t inpsize){
        Array = new T[inpsize];
        size = inpsize;
    }

    MArray<T>(size_t inpsize, const T fillval){
        Array = new T[inpsize];
        size = inpsize;
        this->fill(fillval);
    }
    
};