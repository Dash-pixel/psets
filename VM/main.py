import sys
import VM.functions as functions

def clean(line):
    chars = []
    for char in line:
        if char == '\t':
            continue
        elif char == '/' or char =='\n':
            break
        else:
            chars.append(char)
    if len(chars) == 0:
        return None
    
    arr = ''.join(chars).split()
    return(arr)


def initialize():
    pass


def make_frame(name):


def read_and_write(input_file, output_file):

    with open(input_file, 'r') as input, open(output_file, 'w') as output:
        for line in input:
            if words := clean(line):
                if words[0] == 'function':
                    make_frame(words[1])

if __name__ == '__main__':
    read_and_write(sys.argv[1], sys.argv[2])
