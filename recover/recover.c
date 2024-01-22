#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *raw_pointer = fopen(argv[1], "r");

    char buffer[];

    while (fread (*buffer, sizeof(char), 512, raw_pointer) = sizeof(char)) == 512?

    if buffer [0] == 0xff
// need to write in the buffer the whole card.raw?

// while 512 bytes are not jpeg header, write down a file

    fclose(raw_pointer);

// Write text to the file
    fprintf(filePointer, "Hello, World!\n");

    // Close the file to save the file data
    fclose(filePointer);

    printf("File has been written successfully.\n");

    return 0;
}
