#include <cs50.h>
#include <stdio.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    string key = argv[1];

    for (int i = 0; i != 26; i++){

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
}

// как идея можно использовать разницу чисел
// а код замены можно сразу to_lowercase
// решить задачу математически короч