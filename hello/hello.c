#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("ur name? ");
    printf("hello, %s\n", name);
}