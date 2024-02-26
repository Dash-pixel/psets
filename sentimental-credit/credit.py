# TODO
while (True):
    try:
        number = int(input('Number: '))
    except ValueError:
        continue
    if number > 0 and height < 9:
        break
