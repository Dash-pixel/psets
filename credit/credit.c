#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long credit_number = get_long("Number:");
    string card_type;
    int length = 0;
    long poww(long a, int b);
    int digit;
    int summ = 0;

    if ((340000000000000 <= credit_number && credit_number < 350000000000000) ||
        (370000000000000 <= credit_number && credit_number < 380000000000000))
    {
        card_type = "AMEX\n";
        length = 15;
    }
    else if (5100000000000000 <= credit_number && credit_number < 5600000000000000)
    {
        card_type = "MASTERCARD\n";
        length = 16;
    }
    else if (4000000000000000 <= credit_number && credit_number < 5000000000000000)
    {
        card_type = "VISA\n";
        length = 16;
    }
    else if (4000000000000 <= credit_number && credit_number < 5000000000000)
    {
        card_type = "VISA\n";
        length = 13;
    }
    else
    {
        printf("INVALID\n");
        return (0);
    }

    for (int i = 0; i < length; i++)
    {

        long dosens = poww(10, i);

        if (i % 2 == 0)
        {
            digit = (credit_number % dosens) / (dosens / 10);
        }
        else
        {
            digit = 2 * (credit_number % dosens) / (dosens / 10);
            digit = 2 * digit;

            if (digit > 9)
            {
                digit = (digit % 10) + 1;
            }

        }

        summ += digit;
        printf("%i\n", digit);
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

long poww(long a, int b)
{
    long c = a;
    for (int i = 0; i < b; i++)
    {
        a *= c;
    }
    return (a);
}
