while (True):
    try:
        number = str(int(input('Number: ')))
        break
    except ValueError:
        print("Invalid")
        continue

digits = len(number)
square_sum = 0
check_sum = 0

for i in range(digits):
    if i % 2:
        square_sum += int(number[i])**2
    else
        check_sum += int(number[i])

check_sum += square_sum

if check_sum % 10 == 0:
    print(card_type)
