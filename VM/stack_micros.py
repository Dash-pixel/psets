save_d_to_m = [f"M=D\n"]
decrement_a = [f"A=A-1\n"]
save_m_to_d = [f"D=M\n"]
sumM_D = [f"M=D+M\n"]
minM_D = [f"M=M-D\n"]
negM = [f"M=-M\n"]
notM = [f"M=!M\n"]
andD_M = [f"M=D&M\n"]
orD_M = [f"M=D|M\n"]
decrement_stack = [f"@RAM[0]\nM=M-1\n"]
increment_stack =[f"@RAM[0]\nM=M+1\n"]
select_stack = [f"@RAM[0]\nA=M\n"]

"""" 
sets D to the first value on the stack and 
decrements the stack and points to the next value"""
setD = decrement_stack + save_m_to_d + decrement_a

def compareD_to_M (funct_name, order_number, condition):
    cond_dict = {
        "gt": "JGT",
        "lt": "JLT",
        "eq": "JEQ"
    }
    return[f"""
            D=M-D
            @{funct_name}.setM=-1#{order_number}
            D=D;{cond_dict[condition]}
            {select_stack[0] + decrement_a[0]}
            MD=0
            @{funct_name}.eq_end#{order_number}
            0;JMP
            ({funct_name}.setM=-1#{order_number})
            {select_stack[0] + decrement_a[0]}
            M = -1
            ({funct_name}.eq_end#{order_number})\n"""] 

def def_func(label):
    return [f"({label.upper()})\n"]

def jump_to(place): #go back to previous function in assembly
    return [f"@{place}\n0;JMP\n"]

def offset_pointer_by(number, segment):
    """segment pointer is expected to be selected?"""
    return [f"""
            @{segment}
            D=M
            @{number}
            A=D+M\n
            """]

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def push(number, segment): # this handles just constant = bad. need to also push from different segments
    if segment == "constant":
        save_to_d = [f"@{number}\nD=A\n"]
    
    else:
        save_to_d = offset_pointer_by(number, segment) + ['D=M\n']

    return save_to_d + select_stack + save_d_to_m + increment_stack

def pop(number, segment):
    if segment == "constant":
        return decrement_stack
    else:
        return offset_pointer_by(number, segment) + ["@R1\nM=D\n"] + select_stack + ["D=M\n@R1\nA=M\nM=D"] + decrement_stack
#no need to define this way
# for comparison in ["gt", "lt", "eq"]:
#     globals()[comparison] = lambda funct_name, order_number: setD + compareD_to_M(funct_name, order_number, comparison)

def eq(funct_name, order_number):
    return setD + compareD_to_M(funct_name, order_number, "eq")

def gt(funct_name, order_number):
    return setD + compareD_to_M(funct_name, order_number, "gt")

def lt(funct_name, order_number):
    return setD + compareD_to_M(funct_name, order_number, "lt")


#//////////////////////////////////////////////////////////////////////
#no params = no need for function = calulated once
function_dict = {
    'add': setD + sumM_D,
    'sub': setD + minM_D,
    'neg': select_stack + decrement_a + negM,
    'not': select_stack + decrement_a + notM,
    'and': setD + andD_M,
    'or': setD + orD_M
}

"""def add():
    return setD + sumM_D
    
def sub():
    return setD + minM_D
def neg():
    return select_stack + decrement_a + negM

def bit_not():
    return select_stack + decrement_a + notM

def bit_and():
    return setD + andD_M

def bit_or():
    return setD + orD_M
"""
"""
(LABEL)
    
    @RAM[1 - 4]
    D=M

    (function to be repeated 4 times)

    @RAM[0]
    A=M
    M=D
    @RAM[0] (function to select pointer)
    M=M+1

    (above should be done for RAM[1]-RAM[4] - can be also a function?)


    BUT i also needed to make the new header
    how to do function arguments? need to set pointer to them first thing when function is created

    select pointer and minus 4 to it to set current fucntion frame 

"""