#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>


int main(void)
{
    string text = get_string ("Text: ");
   // printf("Text: %s\n", text);

    int letters = 0, words = 0, sentances = 0;

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

    words ++;

    float L = (float) (100.0 * letters) /((float) words);
    float S = (float) (100.0 * sentances) /((float) words);

    float index = (0.0588 * L) - (0.296 * S) - 15.8;

    float round(index);

    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 15)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }

}