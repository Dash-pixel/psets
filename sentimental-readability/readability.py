import cs50

text = cs50.get_string("Text: ")


L = 0
S = 0
letters = 0
sentences = 0
words = 1


for i in range(len(text)):
    if text[i].isalplha:
        letters += 1
    elif (text[i] == ".") or (text[i] == ".") or (text[i] == "?"):
        sentences += 1
    elif text[i] == " ":
        words += 1


l = letters / (100 * words)
s = sentences / (100 * words)

index = 0.0588 * l - 0.296 * s - 15.8

print("Grade {}".format(index))
