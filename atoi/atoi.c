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

   int digit = char i - '0';
   input[strlen(input)] = '\0';

}

// create 
In the recursive version of convert, start with the last char and convert it into an integer value.
Then shorten the string, removing the last char,
and then recursively call convert using the shortened string as input,
where the next char will be processed.

