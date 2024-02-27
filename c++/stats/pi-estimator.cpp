#include <string>
#include <time.h>
#include <math.h>
#include <random>

inline bool circle_check(float a, float b){
    return (sqrt(a * a + b * b) > 1);
}

int main(){
    srand(time(NULL));

    double sample_size = 100000;
    float in = 0;

    float pi = 0;

    for(int n = 0; n < sample_size; n++){
        in += circle_check((rand() / (float) RAND_MAX), (rand() / (float) RAND_MAX)) == 0;
        pi = 4 * in / n;

        printf("%lf\n", pi);
    }
}