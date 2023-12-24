#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// preferences[i][j] is number of voters who prefer i over j
int preferences[MAX][MAX];

// locked[i][j] means i is locked in over j
bool locked[MAX][MAX];

// Each pair has a winner, loser
typedef struct
{
    int winner;
    int loser;
} pair;

// Array of candidates
string candidates[MAX];
pair pairs[MAX * (MAX - 1) / 2];

int pair_count;
int candidate_count;

// Function prototypes
bool vote(int rank, string name, int ranks[]);
void record_preferences(int ranks[]);
void add_pairs(void);
void sort_pairs(void);
void lock_pairs(void);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: tideman [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i] = argv[i + 1];
    }

    // Clear graph of locked in pairs
    for (int i = 0; i < candidate_count; i++)
    {
        for (int j = 0; j < candidate_count; j++)
        {
            locked[i][j] = false;
        }
    }

    pair_count = 0;
    int voter_count = get_int("Number of voters: ");

    // Query for votes
    for (int i = 0; i < voter_count; i++)
    {
        // ranks[i] is voter's ith preference
        int ranks[candidate_count];

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            if (!vote(j, name, ranks))
            {
                printf("Invalid vote.\n");
                return 3;
            }
        }

        record_preferences(ranks);

        printf("\n");
    }

    add_pairs();
    sort_pairs();
    lock_pairs();
    print_winner();
    return 0;
}

// Update ranks given a new vote
bool vote(int rank, string name, int ranks[])
{
    for(int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i], name) == 0)
        {
            ranks[rank] = i;
            return true;
        }
    }
    return false;
}

// Update preferences given one voter's ranks
void record_preferences(int ranks[])
{
    for (int b = 1; b < candidate_count; b++)
    {
        for (int a = 0; a < b; a++)
        {
            preferences[ranks[a]][ranks[b]]++;
        }
    }
    return;
}

// Record pairs of candidates where one is preferred over the other
void add_pairs(void)
{
    int i = 0;
    for (int b = 1; b < candidate_count; b++)
    {
        for (int a = 0; a < b; a++)
        {

            if (preferences[a][b] > preferences[b][a])
            {
                pairs[i].winner = a;
                pairs[i].loser = b;
                i++;

            }
            else if (preferences[a][b] < preferences[b][a])
            {
                pairs[i].winner = b;
                pairs[i].loser = a;
                i++;
            }

        }
    }
    pair_count = i;
    return;
}
// Sort pairs in decreasing order by strength of victory
void sort_pairs(void)
{
    int a = 0;
    int x_index = 0;
    pair temporary;

    for(int i = 0; i < pair_count; i++)
    {
        for(int j = i; j < pair_count; j++)
        {
            if (a < preferences[pairs[j].winner][pairs[j].loser])
            {
                a = preferences[pairs[j].winner][pairs[j].loser];
                x_index = j;
            }
        }
        temporary = pairs[i];
        pairs[i] = pairs[x_index];
        pairs[x_index] = temporary;
        a = 0;
    }
    return;
}

// Lock pairs into the candidate graph in order, without creating cycles
void lock_pairs(void)
{
        for (int i = 0; i < pair_count; i++)
    {
        int unvisited[MAX] = {};
        bool no_stroke = false;
        int length = 0;

        unvisited[length] = pairs[i].winner;

        while (length >= 0)
        {
            int visiting_candidate = unvisited[length];
            if (pairs[i].loser == visiting_candidate)
                {
                    no_stroke = true;
                }
            length --;

            for (int j = 0; j < candidate_count; j++) //проходимся, находим следующих кандидатов
            {
                if (locked[j][visiting_candidate] == true)
                {
                    length++;
                    unvisited[length] = j;
                }
            }
        }
        if (!no_stroke)
        {
            locked[pairs[i].winner][pairs[i].loser] = true;
        }
    }
}

// Print the winner of the election
void print_winner(void)
{
    for(int i=0; i < candidate_count; i++)
    {
        int not_winner = 0;

        for(int j=0; j < candidate_count; j++)
        {
            not_winner += locked [j][i];
        }

        if (!not_winner)
        {
            printf("%s", candidates[i]);
        }
    }
    return;
}

// locked (winner) (looser)
// i is winner if locked[j 0-->all][i] ==0
// i need to find so that no looser
//  winnner
// L 1
// o
// s
// e 000000
// r
