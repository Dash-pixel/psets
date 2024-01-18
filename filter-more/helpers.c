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
  /*  for (int i = 0; i < height; i++) {

        RGBTRIPLE line[width];

        for (int j = 0; j < width; j++) {

            line[width - j] = image[i][j];
        }

        for (int k = 0; k < width; k++) {

            image[i][k] = line[k];
        }

    }
    */
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
    RGBTRIPLE temp[height][width];

        for (int i = 0; i < height; i++)
    {
            for (int j = 0; j < width; j++)
            {
                temp[i][j] = image[i][j];
            }
    }


    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}



/*            if (i !=0 && j !=0)
            {
                pixels_numb = 9;
            }
            else if (i != 0 && j == 0 || ///)
            {
                pixels_numb = 6;
                middle_green = 0;
                right_green = temp[i-1][0].rgbtGreen + temp[i][0].rgbtGreen + temp[i+1][0].rgbtGreen
            }
            else if (i == 0 && j != 0)
            {
                pixels_numb = 6;

            }*/

/*
        int middle_green = temp[i-1][0].rgbtGreen + temp[i][0].rgbtGreen + temp[i+1][0].rgbtGreen;
        int right_green = temp[i-1][1].rgbtGreen + temp[i][1].rgbtGreen + temp[i+1][1].rgbtGreen;
        image[i][0].rgbtGreen = (middle_green + right_green) /6;
*/
/*            left_green = middle_green;
            middle_green = right_green;
            right_green = temp[i-1][j+1].rgbtGreen + temp[i][j+1].rgbtGreen + temp[i+1][j+1].rgbtGreen;

            image[i][j].rgbtGreen = (left_green + middle_green + right_green)/9;

*/
