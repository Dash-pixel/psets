#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    //open file
    string filename = argv[1];
    int pdf_type [4] = {37, 80, 68, 70};

    FILE *file = fopen(filename, "r");$

    uint8_t buffer[4];

    fread(buffer, 1, 4, file);


    for (i = 0; i < 4; i++)
    {
        buffer[i] 
    }

}
