#include <cs50.h>
#include <stdio.h>
void repeat_char (char charecter, int number_of_times);
int main(void)
{
    int height;
    do
    {
        height = get_int("What is the height? ");
    }
    while (height < 1 || height > 8);

    for (int i = 0; i < height; i++){
        
        printf("\n");
    }

}



//////////////////////////

void repeat_char (char charecter, int number_of_times)
{
    for (int j = 0; j < number_of_times; j++)
    {
        printf("%c", charecter);
    }
}