while (True):
    try:
        number = int(input('Number: '))
        break
    except ValueError:
        print("Invalid")
        continue

def digit_count():
    digits = len(str(number))
    return digits

print(' ' + digits)
