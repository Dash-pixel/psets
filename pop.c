#include <cs50.h>
#include <stdio.h>



int main(void){
    float starting_number = get_float("How many lammas at start ");
    float ending_number = get_float("How many lammas at end ");

    float years = ending_number * 12 / (13 * starting_number);

printf("$fl", years);

}