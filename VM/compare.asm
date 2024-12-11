
D=M-D
@{funct_name}.setM=-1#{order_number}
D=D;JLT
{select_stack()}
MD=0
@{funct_name}.eq_end#{order_number}
0;JMP
({funct_name}.setM=-1#{order_number})
{select_stack()}
M = -1
({funct_name}.eq_end#{order_number})



