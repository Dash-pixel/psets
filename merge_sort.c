
array1[1 3 5 6 7 8 2 4 9];
array2[1 3 - 5 6 - 6 7 - 2 8 - 4 9];


function(Left_start; Right_end)
{
    if array_length = 1
    {
        return;
    }



    Right_start = Left_start + (array_length / 2) + 1

    for(int i = Left_start; i < Right_start; i++)
    {

        if a = b (начальная) or b будет в конце отрезка {

        }

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
