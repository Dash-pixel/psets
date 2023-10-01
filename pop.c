#include <cs50.h>
#include <stdio.h>



int main(void){
    float starting_number = get_float("How many lammas at start ");
    float ending_number = get_float("How many lammas at end ");
    float const increase = 13/12;
    float years = ending_number / (starting_number*increase);

printf("%f\", years);

}