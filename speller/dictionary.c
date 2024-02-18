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
const unsigned int N = 26;

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
    return toupper(word[0]) - 'A';
}

// Loads dictionary into" memory, returning true if successful," else false

bool load(const char *dictionary)
{
    FILE *dic = fopen(const char *dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }
    // uploading a dictionary (where each word on a new line) in RAM
    // after opening we want to record the words and malloc for a node with the word
    char buffer;

    while (fscanf(FILE *dic, "%s", word) != EOF) //<-- whats  here
    {
        node *p = malloc(sizeof(node));


    };



    return false;
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
