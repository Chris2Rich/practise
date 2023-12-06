template <typename T>
class vseptr{
public:
    T* v;
    T* s;
    T* e;

    vseptr(T* val, T* start, T* end){
        v = val;
        s = start;
        e = end;
    }
    
    void operator++(){
        v = ((v+1) > e) * s + ((v+1) < e) * (v+1);
    }
    
    void operator--(){
        v = ((v-1) < s) * e + ((v-1) > s) * (v-1);
    }

};
