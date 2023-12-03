
array1[1 3 5 6 7 8 2 4 9];
array2[];

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
