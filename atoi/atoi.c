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
    if (strlen(input) > 1)
    {
        // instead of deleting elements you can use the string end symbol \0
        input[strlen(input)] = '\0';
    }
    else
    {
        return input[strlen(input)-1] - '0';
    }

    return convert(string input - last_element) + input[strlen(input)-1] - '0'

///



}

// create // string input - last_element
In the recursive version of convert, start with the last char and convert it into an integer value.
Then shorten the string, removing the last char,
and then recursively call convert using the shortened string as input,
where the next char will be processed.


at first we take the last char change it to


we have to use add integers ---> new integer + all old integers, and here we are recursing

// for starters lets just add numbers in string recursivelly.
