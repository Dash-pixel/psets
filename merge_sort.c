array 0 1 2 3 4 5 6 7 8 9
array2

function(Left_start; Right_end)
{
    if array_length = 1
    {
        return;
    }

    Right_start = Left_start + (array_length / 2) + 1;

    Left = Left_start;
    Right = Right_start;

    for(int i = Left_start; i < Left_start + array_length; i++)
    {

        if(array[Left] < array[Right])
        {
        array2[i] = array[Left];
        Left++;
        }

        else if(array[Left] > array[Right])
        {
        array2[i] = array[Right];
        Right++;
        }
    }
    for(int i = Left_start; i < Left_start + array_length; i++)
    {
        array[i] = array2[i];
    }


}
