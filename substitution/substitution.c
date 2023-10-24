#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string key = argv[1];

    for (int i = 0; i != 26; i++)
    {

        if (isalpha(key[i]))
        {
        key[i] = toupper(key[i]) - 64 - i;
        }

        else
        {
            printf("your stuff incorrect");
            return(1);
        }
    }

    string plaintext = get_string("plaintext: ");

    for (int i = 0; plaintext[i] != 0; i++)
    {
        int numberofchar = plaintext[i] - 65;

        plaintext[i] = key[numberofchar];

        printf("%c", plaintext[i]);
    }

}

// моя проблема в том что я референсю числа
// за пределами моего key
// или мне сначала нужно посчитать разницу кода
// с буквой которую представл