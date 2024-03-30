#include <string>
#include <cstring>

const char* test_func(const FILE* const src){

    return "This is a parsed expression.";
}

// Number Of Args , {Script Location, Command ("parse"), File Location, Target Location, Options}

void cli_test_func(int argc, char* argv[]){
    if (argc < 4 || argc > 5){
        printf("Error: Wrong number of arguements.");
        exit(0);
    }

    FILE* src_file = fopen(argv[2], "r");
    FILE* res_file = fopen(argv[3], "w");

    const char* res = test_func(src_file);

    fwrite(res, sizeof(char), strlen(res), res_file);

    fclose(src_file);
    fclose(res_file);
}

int main(int argc, char* argv[]){
    
    if (argc < 2){
        printf("Error: No command given.");
        exit(0);
    }
    
    if (strcmp(argv[1], "test_func") == 0){
        cli_test_func(argc, argv);
    }
}
