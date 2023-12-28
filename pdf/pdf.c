#include <cs50.h>
#include <stdio.h>

int main(int argc, string argv[])
{
    //open file
    string filename = argv[1];

    FILE *file = fopen(filename, "r");$

    uint8_t buffer[4];

    fread(buffer, 1, 4, file);

}
