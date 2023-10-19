#include <cs50.h>
#include <stdio.h>
#include <math.h>


int main(void)
{
    string text = get_string;
    printf("Text: %s\n", text);

    int letters, words, sentances;

    for (int i = 0; text[i] != 0; i++){

        if (text[i] == 32)
        {
            words++;
        }
        else if ((text[i] == 46) || (text[i] == 33) || (text[i] == 63))
        {
            sentances++;
        }
        else if (isalpha(text[i]))
        {
            letters++;
        }
    }
    printf()
}