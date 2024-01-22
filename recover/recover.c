#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *raw_pointer = fopen(argv[1], "r");

    char buffer[];

    while (fread (*buffer, sizeof(char), 512, raw_pointer) = sizeof(char)) == 255?

  if (buffer[0] == 0xff && buffer [1] == 0xd8 && buffer [2] == 0xff && (buffer[3] & 0xf0) == 0xe0)

    fclose(raw_pointer);

// Write text to the file
    fprintf(filePointer, "Hello, World!\n");

    // Close the file to save the file data
    fclose(filePointer);

    printf("File has been written successfully.\n");

    return 0;


    sprintf(filename, "%031.jpg", 2);
    FILE *img = fopen(filename, "w");
    fwrite(data, size, number, outptr);
}
