while (True):
    try:
        number = int(input('Number: '))
        break
    except ValueError:
        print("Invalid")
        continue


digits = len(str(number))
for e
