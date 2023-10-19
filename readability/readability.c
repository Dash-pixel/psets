#include <cs50.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>


int main(void)
{
    string text = get_string ("Text: ");
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

    words ++;

    float L = (float) letters / (100.0 * words);
    float S = (float) sentances / (100.0 * words);

    int index = 0.0588 * L - 0.296 * S - 15.8;

    printf("%i\n", index);

}