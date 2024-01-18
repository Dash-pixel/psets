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
//  RGBTRIPLE avrg_pixl[9];
    RGBTRIPLE temp[height][width];
    int blue_average, red_average, green_average;

        for (int i = 0; i < height; i++)
    {
            for (int j = 0; j < width; j++)
            {
                temp[i][j] = image[i][j];
            }
    }

    for (int i = 0; i < height; i++) {



        for (int j = 0; j < width; j++) {

           left_green = middle_green;
           middle_green = right_green;
           right_green = temp[i-1][j+1] + temp[i][j+1] + temp[i+1][j+1];

           green_average = (((left_green + middle_green + right_green) * 100) + 50)/100;



           // left_green = temp[i-1][j-1] + temp[i][j-1] + temp[i+1][j-1];
           // middle_green = temp[i-1][j] + temp[i][j] + temp[i+1][j];
           // right_green = temp[i-1][j+1] + temp[i][j+1] + temp[i+1][j+1];

// so there we run into problem - there is not enough space in RGBTRIPLE to store summed up numbers
// there is still issue with the NULL pixels, can be solved with an if statement, but its bullshit
// i can do it with an array of the nine pixels?
// maybe could even speed the process up by saving the pixels on the right

        }
    }


    return;
}

// Detect edges
void edges(int height, int width, RGBTRIPLE image[height][width])
{
    return;
}
