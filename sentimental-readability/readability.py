import cs50

text = cs50.get_string("Text: ")


L = 0
S = 0
letters = 0
sentences = 0
words = 1


for i in text: # you can only iterate over a string (not a range) <-hide
    if i.isalpha():
        letters += 1
    elif (i == ".") or (i== "!") or (i == "?"):
        sentences += 1
    elif i == " ":
        words += 1


l = 100 * letters / words
s = 100 * sentences / words

index = round((0.0588 * l) - (0.296 * s) - 15.8)

index = min (index,)

print("Grade {}".format(index))
