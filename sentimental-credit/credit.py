while (True):
    try:
        number = str(int(input('Number: ')))
        break
    except ValueError:
        print("Invalid")
        continue

digits = len(str(number))

for i in range(digits)
