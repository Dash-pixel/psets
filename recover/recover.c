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
      if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && buffer[1] == 0xff && ((buffer[2] & 0xf0) == 0xe0))
      {
        if (i != 0) // why null?
        {
          fclose(filename); //????
        }

        i++;
        sprintf(*filename, "%03i.jpg", i);
        FILE *img = fopen(filename, "w");
        fwrite(*buffer, sizeof(char), 512, *img);
      }

      else if(i > 0)
      {
        fwrite(*buffer, sizeof(char), 512, filename);
      }

    }
}

