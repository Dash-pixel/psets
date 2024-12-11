import sys
import re
c_instruction = {
    #c instruction
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000", 
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "A+D": "0000010", 
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "A&D": "0000000",  
    "D|A": "0010101",
    "A|D": "0010101", 
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "D+M": "1000010",
    "M+D": "1000010",  
    "M-1": "1110010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "M&D": "1000000", 
    "D|M": "1010101",
    "M|D": "1010101",
}
destination = {
    "0": "000", 
    "D": "010",     
    "MD": "011",    
    "A": "100",
    "AM": "101",    
    "AD": "110",   
    "AMD": "111",
    "M": "001",
}
jump = {
    #jump
    "JGT": "001",  
    "JEQ": "010",     
    "JGE": "011",       
    "JLT": "100",     
    "JNE": "101",      
    "JLE": "110",     
    "JMP": "111",    
}
label = {
    "SP": "0000000000000000",       
    "LCL": "0000000000000001",      
    "ARG": "0000000000000010",      
    "THIS": "0000000000000011",     
    "THAT": "0000000000000100",     
    "R0": "0000000000000000",       
    "R1": "0000000000000001",       
    "R2": "0000000000000010",       
    "R3": "0000000000000011",       
    "R4": "0000000000000100",       
    "R5": "0000000000000101",       
    "R6": "0000000000000110",       
    "R7": "0000000000000111",       
    "R8": "0000000000001000",       
    "R9": "0000000000001001",       
    "R10": "0000000000001010",      
    "R11": "0000000000001011",      
    "R12": "0000000000001100",      
    "R13": "0000000000001101",      
    "R14": "0000000000001110",      
    "R15": "0000000000001111",      
    "SCREEN": "0100000000000000", #and all the points after are taken  
    "KBD": "0110000000000000"       
}
variables = set()
taken_address = set()

def to_bin(num): #redo this - makes no sence
    if isinstance(num, int):
        return str(bin(num)[2:].zfill(16))
    if isinstance(num, str):
        print(num)
        return str(bin((num))[2:].zfill(16))

def clean(line):
    chars = []
    for char in line:
        if char == ' ' or char == '\t':
            continue
        elif char == '/' or char =='\n':
            break
        else:
            chars.append(char)

    if len(chars) == 0:
        return None

    chars.append('\n')

    return(''.join(chars))

def add_variables(line):

    for letter in line[1:]:
        if letter.isalpha():
            variables.add(line[1:][:-1])
            break

def add_label(text, number):
    label[text.replace('(', '').replace(')', '').replace('\n', '')] = to_bin(number)
    taken_address.add(to_bin(number))

def give_label(): # TODO this function does not work? needs a new implementation - it gives random adresses

    i = 16

    for variable in variables:

        while to_bin(i) in taken_address: #what this does?
            i += 1

        if variable in label:
            continue

        else:
            label[variable] = to_bin(i)
            i += 1

        #this will never be needed
        #if i >= 2**15:
        #    raise ValueError("Too many variables, ran out of memory")


def assembly_parser(input, output):
    try:
        sentences = []
        with open(input, 'r') as input:

            #initial
            line_counter = 0
            for line in input:
                clean_line = clean(line)
                if clean_line == '' or clean_line == None:
                    continue
                if clean_line[0] == '(':
                    add_label(clean_line, line_counter)
                else:
                    line_counter += 1

                    if clean_line[0] == '@':
                        add_variables(clean_line)

                    sentences.append(clean_line)
        
        give_label()

        with open(output, 'w') as output:

            for sentence in sentences:
                if sentence[0] == '@':
                    if sentence[1:-1] in label:
                        output.write(label[sentence[1:-1]] + '\n')

                    else:
                        output.write(sentence[1:-1] + '\n')
                else:
                    words = []
                    binarywords = ['111']
                    current_string = ''
                    dest_is = jump_is = False


                    for char in sentence:
                        if char == '=':
                            words.append(current_string)
                            current_string = ''
                            dest_is = True


                        elif char == ';':
                            words.append(current_string)
                            current_string = ''
                            jump_is = True

                        elif char == '\n':
                            words.append(current_string)
                            current_string = ''

                        else:
                            current_string += char


                    # here need to change the order -- this is messed up as in hard to achieve
                    # could have done it neeter?

                    if dest_is:
                        binarywords.append(c_instruction[words[1]])
                        binarywords.append(destination[words[0]])
                    else:
                        binarywords.append(c_instruction[words[0]])
                        binarywords.append('000')

                    if jump_is:
                        binarywords.append(jump[words[len(words)-1]])
                    else:
                        binarywords.append('000')

                    # binarywords.append(c_instruction[words[0]])
                    # words = words[1:]
                    
                    # if dest_is:
                    #     binarywords.append(destination[words[0]])
                    #     words = words[1:]
                    # else:
                    #     binarywords.append('000')
                    

                    # if jump_is:
                    #     binarywords.append(jump[words[0]])
                    # else:
                    #     binarywords.append('000')
                    
                    output.write(''.join(binarywords) + '\n')



     
    except IOError:
        print("IOError")
    except FileNotFoundError:
        print("FileNotFoundError")
                    
                    

            


    
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <inputfile> <outputfile>")
        sys.exit(1)

    input = sys.argv[1]
    output = sys.argv[2]

    assembly_parser(input, output)







