from sys import exit
while (True):
    try:
        number = str(int(input('Number: ')))
        break
    except ValueError:
        print("INVALID")

digits = len(number)

if digits == 15 and number[0] == "3" and (number[1] == "4" or number[1] == "7"):
    card_type = "AMEX"
elif digits == 16 and number[0] == "5" and (int(number[1]) in range(1, 6)):
    card_type = "MASTERCARD"
elif ((digits == 13) or (digits == 16)) and (number[0] == "4"):
    card_type = "VISA"
else:
    print("INVALID")
    exit()


check_sum = 0
for i in range(digits):
    index = digits - i - 1
    if i % 2:
        j = int(number[index])*2
        if j > 9:
            j = j - 9
        check_sum += j
    else:
        check_sum += int(number[index])
        

if check_sum % 10 == 0:
    print(card_type)
else:
    print("INVALID")
