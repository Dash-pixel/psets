function(array_length)
{
    if array_length = 1
    {
        array2[a] = array[a];
        return;
    }

    function(array_length/2);

    a = 0;
    b = a + (array_length / 2) + 1

    for(int i = 0; i < array_length; i++)
    {
        if(array[a] < array[b])
        {
        array2[i] = array[a];
        a++;
        }

        else if(array[a] > array[b])
        {
        array2[i] = array[b];
        b++;
        }
    }
}





1 2 3 4
array2 1 -- > array1 (под соответствующим номером)

1 2

1 2 3 4 ...
1 2 3 4 5 6 7 8  --> array2


1234 || 5678 ||| 9 10 11 12 || 13 14 15 16
12345678 ..


