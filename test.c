#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int array_length = 8;
    int array[] = {10, 11, 12, 1, 2, 3, 4, 5};
    int arraya2[array_length];


sorting_inside(Left_start; Right_end)
{
    if array_length = 1
    {
        return;
    }

    int Right_start = Left_start + (array_length / 2);

    int Left = Left_start;
    int Right = Right_start;


for(int i = Left_start; i < Right_end; i++)
    {

        if (Left == Right_start)
        {
            array2[i] = array[Right];
            Right++;
        }
        else if (Right == Left_start + array_length)
        {
            array2[i] = array[Left];
            Left++;
        }
        else
        {
            if(array[Left] < array[Right])
            {
            array2[i] = array[Left];
            Left++;
            }

            else if(array[Left] >= array[Right])
            {
            array2[i] = array[Right];
            Right++;
            }
        }
    }

    for(int i = Left_start; i < Right_end; i++)
    {
        array[i] = array2[i];
    }
}
}
