#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if ((argc < 2) || (argc > 2))
    {
        printf("Usage: ./substitution key");
        return(1);
    }

    string key = argv[1];
    char check[27] = {'\0'}; // Initializes all elements to the null character '\0'


    for (int i = 0; i != 26; i++)
    {

        if (isalpha(key[i]))
        {
            key[i] = toupper(key[i]);

            if (check[key[i] - 65] == 0)
            {
                check[key[i] - 65] = 1;
            }
            else
            {
                printf("reapeted values");
                return(1);
            }
        }

        else
        {
            printf("your stuff incorrect");
            return(1);
        }
    }

    string plaintext = get_string("plaintext: ");
    printf("ciphertext: ");


    for (int i = 0; plaintext[i] != 0; i++)
    {
        if (isupper(plaintext[i]))
        {
            plaintext[i] = key[plaintext[i] - 65];

            printf("%c", plaintext[i]);
        }
        else if (islower(plaintext[i]))
        {
            plaintext[i] = key[plaintext[i] - 97] + 32;

            printf("%c", plaintext[i]);
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}
