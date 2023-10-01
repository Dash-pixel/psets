#include <cs50.h>
#include <stdio.h>



int main(void){
    int starting_number = get_int("How many lammas at start ");
    int ending_number = get_int("How many lammas at end ");

    int years_to_get_to_goal = ending_number * 12 / (13 * starting_number);

printf(years_to_get_to_goal);

}