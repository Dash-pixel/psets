#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    char last_element = input[strlen(input)-1];

    if (strlen(input) > 1)
    {
        input[strlen(input)] = '\0';
    }
    else
    {
        return input[strlen(input)-1] - '0';
    }

    return convert(input) + last_element - '0';

}

// create // string input - last_element

// for starters lets just add numbers in string recursivelly.
