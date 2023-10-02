#include <cs50.h>
#include <stdio.h>



int main(void){
    int starting_number = get_int("How many lammas at start ");
    int ending_number = get_int("How many lammas at end ");
    int years;

    if (starting_number < ending_number){
        starting_number = starting_number*13/12;
        years ++;
    }
print(years)
}