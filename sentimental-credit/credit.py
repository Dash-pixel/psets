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

if digits == 15 and number[0] == "3" and (number[1] == 4 or number[1] == 7):
    card_type = "AMEX"
elif digits == 16 and number[0] == "5" and (number[1] in range(1, 5)):
    card_type = "MASTERCARD"

for i in range(digits):
    if i % 2:
        square_sum += int(number[i])**2
    else
        check_sum += int(number[i])

check_sum += square_sum

if check_sum % 10 == 0:
    print(card_type)
