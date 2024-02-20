// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table ------- reading the dict.
const unsigned int N = 210; // 2*3*5*7

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
    // 2*3*5*7
    // make a summ of letters in a word
    int word_summ = 0;

    for (int i = 0; word[i] != \0; i++)
    {
        word_summ += word[i];
    }

    word_summ % 2

    return;
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

    while (fscanf(FILE *dic, "%s", word_from_dic) != EOF) //<-- whats  here
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
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
