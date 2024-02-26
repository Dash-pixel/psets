while (True):
    try:
        number = int(input('Number: '))
        break
    except ValueError:
        print("Invalid")
        continue

def digit_count():
    number = str(number)
    digits = len(number)

print(' ' + digits)
