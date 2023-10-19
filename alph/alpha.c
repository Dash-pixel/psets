#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string word = get_string("Word: ");
// abc whether alphabetical order
    int i = 0;
    while (word[i] < word[i+1])
    {
        i++;
    }

    if (word[i+1] == 0)
    {
        printf("Yes");
    }
    else
    {
        printf("No");
    }

}

// we have to check whether word i+1  > word i
// untill the end of the string
// unless we prooved otherwise before the end of the sting
// but if it reaches \0 - printf(yes)
// but zero cannot be higher than i-1


//// for (int i = 0; word[i] < word[i+1]; i++){