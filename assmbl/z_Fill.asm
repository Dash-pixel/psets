(MAIN)
    @KBD
    D=M
    @DECOLOR
    D;JEQ
    @COLOR
    D;JGT

(DECOLOR)
    @SCREEN
    D=A
    @pixel_pointer
    AM=D
    M=0


    (DECOLORING_LOOP)
        @pixel_pointer
        AM=M + 1
        M=0

        D=A
        @DECOLORING_LOOP
        M=D

        @KBD
        D=A

        @DECOLORING_LOOP
        0=D-M;JGT
    @MAIN
    0;JMP

(COLOR)
    @SCREEN
    D=A
    @pixel_pointer
    AM=D
    M=-1


    (COLORING_LOOP)
        @pixel_pointer
        AM=M + 1
        M=-1

        D=A
        @COLORING_LOOP
        M=D

        @KBD
        D=A

        @COLORING_LOOP
        0=D-M;JGT
    @MAIN
    0;JMP
