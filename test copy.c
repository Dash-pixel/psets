#include <cs50.h>
#include <stdio.h>
#include <string.h>

void sorting_inside(int Left_start, int Right_end);

    int array[] = {10, 11, 12, 1, 2, 3, 4, 5, 8, 9};
    int array2[10];

int main(void)
{
    {
    int pref_count = (candidate_count * (candidate_count - 1) / 2);
    int a = 0;
    int exchange_number = 0;

    for(int i = 0; i < pref_count; i++)
    {
        for(int j = i; j < pref_count; j++)
        {
            if (a > preferences[pairs[j].winner][pairs[j].loser])
            {
                a = preferences[pairs[j].winner][pairs[j].loser];
                exchange_number = j;
            }
        }

        preferences[pairs[exchange_number].winner][pairs[exchange_number].loser] = preferences[pairs[i].winner][pairs[i].loser];
        preferences[pairs[i].winner][pairs[i].loser] = a;
    }
}



