// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>

#include "dictionary.h"

#include <stdio.h>  // For FILE, fopen, fclose, fscanf, EOF
#include <stdlib.h> // For malloc, free, NULL
#include <string.h> // For strcmp, strcpy

// counts number of dictiona
int counter = 0;

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table ------- reading the dict.
const unsigned int N = 2000; //

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    // return true if word in dict
    // IMPORTAINT TO LOWER CASE HERE
    node *p = table[hash(word)];

    int a = 0;
    char word_to_lower[LENGTH + 1] = {0};

    while (word[a])
    {
        word_to_lower[a] = tolower(word[a]); // Convert each character to lowercase
        a++; // Move to the next character
    }


   while (p != NULL)
    {
        if(strcmp(word_to_lower, p -> word) == 0)
        {
            return true;
        }
        p = p -> next;
    }
/// нужно переписать чтобы были маленькие буквы
    return false;

}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
    unsigned int summ = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        summ += (tolower(word[i])) * (i + 1); //maybe multiply here?? but is there a point
        // how to make a trully unique identity??
    }

    return (summ % N);
}

// Loads dictionary into memory, returning true if successful, else false

bool load(const char *dictionary)
{
    FILE *dic = fopen(dictionary, "r");
    if (dic == NULL)
    {
        return false;
    }

    char word_from_dic[LENGTH + 1] = {0}; // how to make sure that there is enough space

    while (fscanf(dic, "%s", word_from_dic) != EOF) //<-- how do i read word one at a time so that no segment fault
    {
        node *p = malloc(sizeof(node));
        if (p == NULL)
        {
            return false;
        }

        strcpy(p -> word, word_from_dic);


        int n = hash(word_from_dic);

        // find the last element pointer in the bucket
        p -> next = table[n];
        table[n] = p;
        counter++;

    };
/////////////////////////////////////////////////////////////////////////////
    /*   for (int i = 0; i < N; i++) { // Iterate over each bucket
        int count = 0; // Initialize node counter for the current bucket
        double
        node *cursor = table[i]; // Start with the first node in the bucket

        // Count nodes in the current linked list
        while (cursor != NULL) {
            count++;
            cursor = cursor->next; // Move to the next node
        }

        printf("Bucket %d has %d nodes\n", i, count); // Print the count for this bucket
    }
    */
/////////////////////////////////////////////////////////////////////////////////////////////////////////

    fclose(dic);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    // пока что непонятно как -- я не могу делать глобальные вариаблы вроде как
    return counter;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    node *temp;

    for (int i = 0; i < N; i++)
    {
        node *p = table[i];

        while (p->next!=NULL)
        {
            temp = p -> next;
            free(p);
            p = temp;
        }

    }
    return true;
}
