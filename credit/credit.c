#include <cs50.h>
#include <stdio.h>

int main(void)
{
// American Express cards start with 34 or 37, /// American Express cards have 15 digits
// MasterCard cards start with 51, 52, 53, 54, or 55, /// MasterCard has 16 digits,
// Visa cards start with 4 /// Visa has either 13 or 16 digits.
    long credit_number = get_long("Number:");

    if (340000000000000 <= credit_number < 350000000000000 || 370000000000000 <= credit_number < 350000000000000)
    {
        prinf("AMEX\n");
    }
    else if (5100000000000000 <= credit_number < 5600000000000000)
    {

    }
    else if (4000000000000000 <= credit_number < 5000000000000000 || 40000000000000 <= credit_number < 50000000000000)
    {

    }
    else
    {
        prinf("INVALID\n");
    }



// превратить все числа числа в отдельные диджиты
//        for ( i = 1; i < 5; i++)

}

