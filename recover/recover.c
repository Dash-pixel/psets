#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    FILE *raw_pointer = fopen(argv[1], "r");

    char buffer[512];
    // just declaring how many elements in buffer, fread utterates through by itself
    int i = 0;
    char *filename = malloc(sizeof(char) * 8); // why this needed?


    while(fread(buffer, sizeof(char), 512, raw_pointer) == 512)
    {
      if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[1] == 0xff) && ((buffer[2] & 0xf0) == 0xe0))
      {
        //the case where we start a new jpeg
      }
      else if
      {
        //the case where we continue to write up the files
      }
      else
      {
        //the first case where we did not yet find a jpeg
      }

    }
}

