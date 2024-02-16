#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average_color;

    for (int i = 0; i < height; i++) {

        for (int j = 0; j < width; j++) {

            average_color = image[i][j].rgbtGreen + image[i][j].rgbtRed + image[i][j].rgbtBlue;
            average_color =  ((average_color * 100) / 3 + 50)/100;
            image[i][j].rgbtGreen = image[i][j].rgbtRed = image[i][j].rgbtBlue = average_color;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {

        RGBTRIPLE temp;
        int half_of_width = width / 2;
        int lastpixel_index = width - 1;

        for (int j = 0; j < half_of_width; j++) {

            temp = image[i][j];
            image[i][j] = image[i][lastpixel_index - j];
            image[i][lastpixel_index - j] = temp;

        }

    }

    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE temp_image[height][width];

    for (int i = 0; i < height; i++) {

        for (int j = 0; j < width; j++) {
            temp_image[i][j] = image[i][j];
        }
    }

    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            int division_factor = 0;
            unsigned int red = 0;
            unsigned int green = 0;
            unsigned blue = 0;

            for (int k = i - 1; (k <= i + 1) && (k < height); k++)
            {

                for (int l = j - 1; (l <= j + 1) && (l < width); l++)
                {
                    if ((k >= 0) && (l >= 0)){

                        red += temp_image[k][l].rgbtRed;
                        green += temp_image[k][l].rgbtGreen;
                        blue += temp_image[k][l].rgbtBlue;
                        division_factor ++;
                    }
                }
            }

            image[i][j].rgbtRed = (float) red/division_factor + 0.5;
            image[i][j].rgbtGreen = (float) green/division_factor + 0.5;
            image[i][j].rgbtBlue = (float) blue/division_factor + 0.5;
        }
    }

    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    for (i = 0; i < height; i++) {
        for (j = 0; j < width; j++) {

            for (k = -1; k < 1; k++) {
                for (l = -1; l < 1; l++) {

                    multiplyer 
                    l * image[i + k][j + l]red

            // we need -1 0 1
                    // -2 0 2
                    // -1 0 1

                }
            }
        }
    }
    return;
}

