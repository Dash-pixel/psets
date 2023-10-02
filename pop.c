#include <cs50.h>
#include <stdio.h>

int main(void){
    float starting_number = get_float("How many lammas at start ");
    float ending_number = get_float("How many lammas at end ");
    float const n = 1/12;
    float years;

    if (starting_number < ending_number){
        starting_number = starting_number + n;
        years ++;
    };
printf("$f\n", years);
}