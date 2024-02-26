# TODO
'''first prompt the user with get_int for the half-pyramid’s height, a positive integer between 1 and 8, inclusive.

If the user fails to provide a positive integer no greater than 8, you should re-prompt for the same again.

Then, generate (with the help of print and one or more loops) the desired half-pyramids.

Take care to align the bottom-left corner of your pyramid with the left-hand edge of your terminal window,
and ensure that there are two spaces between the two pyramids,
and that there are no additional spaces after the last set of hashes on each row.'''

while (True):
    try:
        height = int(input('Height:\n'))
    except ValueError:
        continue
    if height > 0 and height < 9:
        break
for i in range(height):
    print(" "*(height-i) + "#" * (i + 1) + "  " + "#" * (i + 1))
