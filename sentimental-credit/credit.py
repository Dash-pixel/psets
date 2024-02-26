while (True):
    try:
        number = str(int(input('Number: ')))
        break
    except ValueError:
        print("Invalid1")
        continue

digits = len(number)
square_sum = 0
check_sum = 0

if digits == 15 and number[0] == "3" and (number[1] == "4" or number[1] == "7"):
    card_type = "AMEX"
elif digits == 16 and number[0] == "5" and (number[1] in str(range(1, 6))):
    card_type = "MASTERCARD"
elif (digits == 13 or 16) and (number[0] == "4"):
    card_type = "VISA"
else:
    print("Invalid2")


for i in range(digits): # итак, мы хотим начать не с первого а с последнего числа
# [0, 1, 2, 3] - length is 4
# i = 4 --> length - i
    index = digits - i
    if i % 2:
        j = int(number[i])*2
        if j > 9:
            j = j - 10 + 1
        square_sum += j
    else:
        check_sum += int(number[i])

check_sum += square_sum

if check_sum % 10 == 0:
    print(card_type)
else:
    print("Invalid3")
