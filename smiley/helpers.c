#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    for(int i = 0; i < width; i++)
    {
        for(int j = 0; j < width; j++)
        {
            if (image[i][j].rgbtGreen = 0x00)
            {
                    image.rgbtGreen = 0xFF;
                    image.rgbtRed = 0xFF;
            }
        }
    }

}
