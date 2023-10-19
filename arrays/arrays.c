#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n = get_int("What's your size? ");
    int array[n]; // different things - this is length of array
    array[0] = 1; // this is the first element of array

    printf("%i\n", array[0]);

    for (int i = 1; i < n; i++){
        array[i] = array[i-1] * 2;

        printf("%i\n", array[i]);
    }

}