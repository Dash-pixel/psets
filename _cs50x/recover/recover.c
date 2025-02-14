#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
  if (argc != 2)
  {
    printf("Usage: ./recover IMAGE\n");
    return 1;
  }
  FILE *raw_pointer = fopen(argv[1], "r");
  char *filename = malloc(sizeof(char) * 8); // why this needed? NEED TO WRITE FILE NAME IN STRING
  unsigned char buffer[512]; // just declaring how many elements in buffer, fread iterates on its own
  int i = 0; //used for image names
  FILE *img; //just so that compiler does not bug with "undefined";


  while(fread(buffer, sizeof(char), 512, raw_pointer) == 512) //are buffer and raw_pointer with *?
  {
    if ((buffer[0] == 0xff) && (buffer[1] == 0xd8) && (buffer[2] == 0xff) && ((buffer[3] & 0xf0) == 0xe0))
    {
      //the case where we start a new jpeg
      if (i != 0) //we need to first close the old jpeg, if it exists
        {
          fclose(img); //here be sure to use file, not file name
        }
      sprintf(filename, "%03i.jpg", i); // is * needed?
      img = fopen(filename, "w"); // how should i write this line?
      fwrite(buffer, sizeof(char), 512, img); // what here?
      i++;
    }
    else if(i > 0)
    {
      //the case where we continue to write up the files
      fwrite(buffer, sizeof(char), 512, img); // we are here as if overwriting the same pointer, but pointer shifts every time by itself
    }

  }
  fclose(img);
  fclose(raw_pointer); // explain each one
  free(filename);
}

