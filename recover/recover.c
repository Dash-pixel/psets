#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *raw_pointer = fopen(argv[1], "r");

    fread (*buffer, sizeof(BYTE), 512, raw_pointer)
// need to write in the buffer the whole card.raw?

// while 512 bytes are not jpeg header, write down a file
}
