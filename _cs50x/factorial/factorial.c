#include <stdio.h>
#include <cs50.h>

int factorial (int number);

int main(void)
{


}

int factorial (int number)
{
    if (number == 1){
        return 1;
    }

    return factorial(number - 1) * number;
}