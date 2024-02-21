// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

#include <stdio.h>  // For FILE, fopen, fclose, fscanf, EOF
#include <stdlib.h> // For malloc, free, NULL
#include <string.h> // For strcmp, strcpy

// counts number of dictiona

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table ------- reading the dict.
const unsigned int N = 2310; //

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // return true if word in dict
    // IMPORTAINT TO LOWER CASE HERE
    char word_lower[LENGTH + 1];

    for (int i = 0; word[i] != '\0'; i++)
    {
        word_lower[i] = tolower(word[i]);
    }

    for (node *p = table[hash(word_lower)]; p -> next != NULL; p = p -> next)
    {
        if(strcmp(word_lower, p -> word) == 0)
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
        summ += word[i] * (i + 1); //maybe multiply here?? but is there a point
        // how to make a trully unique identity??
        ///
    }

    int n =
    return n;

    //why is this a shit idea?
    //because the summ is the same for words with the same letters and therefore will have the same remainders
}

// Loads dictionary into memory, returning true if successful, else false

bool load(const char *dictionary)
{
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }

    char *word_from_dic = NULL;

    while (fscanf(dic, "%s", word_from_dic) != EOF) //<-- whats  here
    {
        node *p = malloc(sizeof(node));
        if (p == NULL)
        {
            return false;
        }

        strcpy(p -> word, word_from_dic); // at string_copy happened a segmentation fault // why?
        // p->word is a fixed-size array, make sure word_from_dic does not exceed this size

        int n = hash(word_from_dic);

        // find the last element pointer in the bucket
        p -> next = table[n];
        table[n] = p;
    };
    fclose(dic);
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
    node *temp;

    for (int i = 0; i < N; i++)
    {

        for (node *p = table[i]; p->next!=NULL; p = temp)
        {
            temp = p -> next;
            free(p);
        }

    }
    return true;
}
