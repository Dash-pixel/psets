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

//////////////////////////////////////////////////////////////////////////////////////////

    int height_min1 = height - 1, width_min1 = width - 1;

    for (int i = 1; i < height_min1 ; i++)
    {

        //can i itterate by color / property? smth smth do three times .color (thats the mega circle)


        for (int j = 0; j < width; j++)
        {
            if (j !=0 && j ! width)
            {
                pixels_numb = 9;
            }
            else if (j == 0)
            {
                pixels_numb = 6;
                middle_green = 0;
                right_green = temp[i-1][0].green + temp[i][0].green + temp[i+1][0].green
            }

            left_green = middle_green;
            middle_green = right_green;
            right_green = temp[i-1][j+1].green + temp[i][j+1].green + temp[i+1][j+1].green;

            image[i][j].green = ((((left_green + middle_green + right_green) * 100) + 50)/9)/100;

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
                right_green = temp[i-1][0].green + temp[i][0].green + temp[i+1][0].green
            }
            else if (i == 0 && j != 0)
            {
                pixels_numb = 6;

            }*/
