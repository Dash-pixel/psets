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
        key[i] = tolower(key[i]);
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
        i = key [i] - 65;

        printf("%c ", plaintext[i]);
    }

}


// so we