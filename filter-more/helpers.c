#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    int average_color;

    for (int i = 0; i < height; i++) {

        for (int j = 0; j < width; j++) {

            average_color = (((image[i][j].rgbtGreen + image[i][j].rgbtRed + image[i][j].rgbtBlue) * 100 / 3) + 50)/100;
            image[i][j].rgbtGreen = average_color;
            image[i][j].rgbtRed = average_color;
            image[i][j].rgbtBlue = average_color;

        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++) {

        

        for (int j = 0; j < width; j++) {
            image[i][j]
        }

        for (int k = 0; k < width; k++) {
            image[i][j]
        }

    }


    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
