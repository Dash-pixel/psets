#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int array_length = argc - 1;
    int Leftstart

    for(int i = Left_start; i < Left_start + array_length; i++)
    {

        if (Left != Right_start)
        {

            if(array[Left] < array[Right])
            {
            array2[i] = array[Left];
            Left++;
            }

            else if(array[Left] > array[Right])
            {
            array2[i] = array[Right];
            Right++;
            }
        }
        else
        {
            array2[i] = array[Right];
            Right++;
        }

    }
}
