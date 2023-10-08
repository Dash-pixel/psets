#include <cs50.h>
#include <stdio.h>

int main(void)
{
// American Express cards start with 34 or 37, /// American Express cards have 15 digits
// MasterCard cards start with 51, 52, 53, 54, or 55, /// MasterCard has 16 digits,
// Visa cards start with 4 /// Visa has either 13 or 16 digits.
    long credit_number = get_long("Number:");
    int length = 0;

    if ((340000000000000 <= credit_number && credit_number< 350000000000000) || (370000000000000 <= credit_number && credit_number < 380000000000000))
    {
        string card_type = "AMEX\n";
        length = 15;
    }
    else if (5100000000000000 <= credit_number && credit_number < 5600000000000000)
    {
        string card_type = "MASTERCARD\n";
        length = 16;
    }
    else if (4000000000000000 <= credit_number && credit_number < 5000000000000000)
    {
        string card_type = "VISA\n";
        length = 16;
    }
    else if (4000000000000 <= credit_number && credit_number < 5000000000000)
    {
        string card_type = "VISA\n";
        length = 13;
    }
    else
    {
        printf("INVALID\n");
        return(0);
    }


int digit;
int summ;

    for (int i = 0; i < length; i++){
        if (i % 2 == 0)
        {
            digit = credit_number % (pow(10, i));
        }
        else
        {
            digit = 2 * credit_number % (pow(10, i));

            if (digit > 9)
            {
                digit = (digit % 10) + 1;
            }
        }

        summ += digit;
    }

    if (summ % 10 == 0)
    {
        printf("%s", card_type);
    }
    else
    {
        printf("INVALID\n");
    }

}

 long pow (long a, int b){

    for (int i = 0; i < b; i++){
        a = a * a;
    }

 }