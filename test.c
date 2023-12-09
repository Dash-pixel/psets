#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int array[6]{2, 5, 7, 3, 8, 9};
    int array2[6];

    Right_start = Left_start + (array_length / 2) + 1;

    Left = Left_start;
    Right = Right_start;

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
