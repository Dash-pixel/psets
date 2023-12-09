array
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

    for(int i = Left_start; i < Right_start; i++)
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
}
