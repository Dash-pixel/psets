#include <stdio.h>
#include <cs50.h>

int factorial (int number);

int main(void)
{


}

int factorial (int number)
{
    if (number == 0){
        return;
    }

    number = factorial(number - 1) * number;
}