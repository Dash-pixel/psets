#include <cs50.h>
#include <stdio.h>

int main(void)
{
// American Express cards start with 34 or 37, /// American Express cards have 15 digits
// MasterCard cards start with 51, 52, 53, 54, or 55, /// MasterCard has 16 digits,
// Visa cards start with 4 /// Visa has either 13 or 16 digits.
    long credit_number = get_long("Number:");

    if ((340000000000000 <= credit_number && credit_number< 350000000000000) || (370000000000000 <= credit_number && credit_number < 380000000000000))
    {
        printf("AMEX\n");
    }
    else if (5100000000000000 <= credit_number && credit_number < 5600000000000000)
    {

    }
    else if ((4000000000000000 <= credit_number && credit_number < 5000000000000000) || (4000000000000 <= credit_number && credit_number < 5000000000000))
    {

    }
    else
    {
        printf("INVALID\n");
    }

even_number
    for (int i = 0; i < (length / 2); i++){
// 222222 --- legth % 2
// 12 12 12 12 12 1

        odd_number = number / (pow(100, i));

        even_number = 2 * number / (pow(100, i)*10);
//
// number / 100^( )
// number / 10
        if (even_number > 9)
        {
            even_number = (even_number % 10) + 1;
        }

        summ += even_number + odd_number;
    }


}

