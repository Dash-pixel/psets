#include <cs50.h>
#include <stdio.h>



int main(void){
    float starting_number = get_int("How many lammas at start ");
    float ending_number = get_int("How many lammas at end ");

    float years_to_get_to_goal = ending_number * 12 / (13 * starting_number);

printf(years_to_get_to_goal);

}