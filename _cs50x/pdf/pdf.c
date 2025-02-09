#include <cs50.h>
#include <stdint.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    //open file
    string filename = argv[1];
    int pdf_type [4] = {37, 80, 68, 70};

    FILE *file = fopen(filename, "r");

    uint8_t buffer[4];

    fread(buffer, 1, 4, file);


    for (int i = 0; i < 4; i++)
    {
        if (buffer[i] != pdf_type[i])
        {
            printf("not pdf");
            return 1;
        }
    }

    printf("pdf\n");
    return 0;

}
