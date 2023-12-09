#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    int array_length = 6;

    int array[] = {3, 4, 5, 0, 1, 2};
    int array2[array_length];

    int Left_start = 0;
    int Right_start = Left_start + (array_length / 2);

    int Left = Left_start;
    int Right = Right_start;


    for(int i = Left_start; i < Left_start + array_length; i++)
    {

        if ((Left != Right_start) || (Right != Left_start + array_length))
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
        else if (Left == Right_start)
        {
            array2[i] = array[Right];
            Right++;
        }
        else if (Right == Left_start + array_length)
        {
            array2[i] = array[Left];
            Left++;
        }

         // if right is smaller than 6, else just increase left and write

    }

    for(int i = Left_start; i < Left_start + array_length; i++)
    {
        printf("%i\n", array2[i]);
    }

}
