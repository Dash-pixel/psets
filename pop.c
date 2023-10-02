#include <cs50.h>
#include <stdio.h>

int main(void){
    float starting_number = get_float("How many lammas at start ");
    float ending_number = get_float("How many lammas at end ");
    float n = 2; //13/12;
    float years = 0;

    while (starting_number < ending_number){
        starting_number = starting_number*n;
        years++;
        printf("while");
    };

printf("main void");
printf("%f\n", years);
}