unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    // return toupper(word[0]) - 'A';
    // 2*3*5*7*11
    unsigned int summ = 0;

    for (int i = 0; word[i] != '\0'; i++)
    {
        summ += (word[i]-'a') * (i + 1); //maybe multiply here?? but is there a point
        // how to make a trully unique identity??
        ///
        for_check = word[i];
    }
    int n = (1155*(summ % 2) + 385*(summ % 3) + 77*(summ % 5) + 11*(summ % 7) + (summ % 11)); //n
    return n;

}
