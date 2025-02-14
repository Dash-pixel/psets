#include <stdio.h>
#include <stdlib.h>

#include "helpers.h"

int main(int argc, char *argv[]) // this is a pointer, why -- used to be string
{
    // ensure proper usage
    if (argc != 3)
    {
        printf("Usage: colorize infile outfile\n");
        return 1;
    }

    // remember filenames
    char *infile = argv[1];
    char *outfile = argv[2];

    // open input file
    FILE *inptr = fopen(infile, "r"); //why is it the pointer to RAM
    if (inptr == NULL) //fopen returns NULL when cannot open file
    {
        printf("Could not open %s.\n", infile);
        return 4;
    }

    // open output file
    FILE *outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        printf("Could not create %s.\n", outfile);
        return 5;
    }
////////////////////////////////////////////////////////////////////////////////////
    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf; // file header data_type ----> bf is declared --> found place for bf
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);
    // &bf where saves --- sizeof from inptr --- 1 это кол-во отрезков???
    //&bf find place where stored
    //inptr - stores infile place

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi; // infoheader -- pointer after reading fileheader moves to the next
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 ||
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        printf("Unsupported file format.\n");
        return 6;
    }
//////////////////////////////////////////////////////////////
    int height = abs(bi.biHeight); //what the fuck is abs -- a module in math. (why its not done with width?)
    int width = bi.biWidth;
//////////////////////////////////////////////////////////////--- did not do futher than that

    // allocate memory for image
    RGBTRIPLE (*image)[width] = calloc(height, width * sizeof(RGBTRIPLE));
    if (image == NULL) /// dont get it
    {
        printf("Not enough memory to store image.\n");
        fclose(outptr);
        fclose(inptr);
        return 7;
    }

    // determine padding for scanlines
    int padding =  (4 - (width * sizeof(RGBTRIPLE)) % 4) % 4;

    // iterate over infile's scanlines
    for (int i = 0; i < height; i++)
    {
        // read row into pixel array
        fread(image[i], sizeof(RGBTRIPLE), width, inptr);

        // skip over padding
        fseek(inptr, padding, SEEK_CUR);
    }

    colorize(height, width, image);

    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);

    // write new pixels to outfile
    for (int i = 0; i < height; i++)
    {
        // write row to outfile
        fwrite(image[i], sizeof(RGBTRIPLE), width, outptr);

        // write padding at end of row
        for (int k = 0; k < padding; k++)
        {
            fputc(0x00, outptr);
        }
    }

    // free memory for image
    free(image);

    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    return 0;
}
