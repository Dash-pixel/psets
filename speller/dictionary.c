// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// counts number of dictiona

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table ------- reading the dict.
const unsigned int N = 2310; // 2*3*5*7*11

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // return true if word in dict
    // IMPORTAINT TO LOWER CASE HERE
    for (int i = 0; word[i] != '\0'; i++)
    {
        word[i] = tolower(word[i]);
    }

    for (char *p = table[hash(*word)]; p != NULL; p = p -> next)
    {
        if(strcmp(word, p -> word) == 0)
        {
            return true;
        }
    }

    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
    // 2*3*5*7*11
    unsigned int summ = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        summ += word[i];
    }

    int n = (1155*(summ % 2) + 385*(summ % 3) + 77*(summ % 5) + 11*(summ % 7) + (summ % 11));
    return n;
}

// Loads dictionary into memory, returning true if successful, else false

bool load(const char *dictionary)
{
    FILE *dic = fopen(const char *dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }

    char *word_from_dic;

    while (fscanf(dic, "%s", word_from_dic) != EOF) //<-- whats  here
    {
        node *p = malloc(sizeof(node));
        if (*p == NULL)
        {
            return false;
        }

        char *strcpy(p -> word, word_from_dic);

        int n = hash(word_from_dic);

        // find the last element pointer in the bucket
        p -> next = table[n];
        table[n] = p;


    };



    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // пока что непонятно как -- я не могу делать глобальные вариаблы вроде как
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    for (i = 0; i < N; i++)
    {
        table[i]
    }
    return false;
}
