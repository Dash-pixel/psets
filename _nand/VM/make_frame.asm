

(FUNCTION NAME) // NEEDED?
    
    @RAM[1 - 4]
    D=M

    (function to be repeated 4 times)

    @RAM[0]
    A=M
    M=D
    @RAM[0] (function to select pointer)
    M=M+1

////
# for push command -- also have the number given {number} to offset from the pointer
@LCL
D=M
@{number}
A=D+M
D=M


///
pop
what should the policy be for temp registers?

""""""@{segment} 
D=M
@{number}
D=D+M"""""" done by segment pointer

@R1
M=D // setting the offset to M in temp register

@stack // setting the popped value to D
D=M
@R1
A=M
M=D

could i have done it without extra register? i think not, because of extra effort in selecting the stack?
