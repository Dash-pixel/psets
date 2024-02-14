#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  FILE *raw_pointer = fopen(argv[1], "r");
  char *filename = malloc(sizeof(char) * 8); // why this needed? NEED TO WRITE FILE NAME IN STRING
  char buffer[512]; // just declaring how many elements in buffer, fread utterates through by itself
  int i = 0; //used for image names


  while(fread(buffer, sizeof(char), 512, raw_pointer) == 512)
  {
    if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[1] == 0xff) && ((buffer[2] & 0xf0) == 0xe0))
    {
      //the case where we start a new jpeg
      if (i != 0) //we need to first close the old jpeg, if it exists
        {
          fclose(filename);
        }
      sprintf(*filename, "%03i.jpg", i);
      FILE *img = fopen(filename, "w");
      fwrite(*buffer, sizeof(char), 512, *img);
      i++;
    }
    else if
    {
      //the case where we continue to write up the files
      fwrite(*buffer, sizeof(char), 512, *img); // we are here as if overwriting the same pointer, but pointer shifts every time by itself
    }

  }
}

