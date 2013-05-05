from sys import argv

def populate(codefile):

    '''(file open for reading) -> list of str

    Read the Opcodes from a portable executable(PE) and return a list where each
    list of Opcodes are arranged next to each other

    Precondition:

    '''

    #skip over the header
    asm = open(codefile).read()

    opcode_list = ["mov", "equ", "proc", "neg", "add", "push", "jmp", "dec", "int", "cmp", "call", "or", "pop", "rep", "xor", "out", "in", "db", "sub", "lea", "jne", "retf", "sub", "sbb", "clc", "xchg", "jb", "dw", "je"]
    
    code = []

    for n in codefile :
        #search for the opcode file and append to code
        opcode = 0

        for opcode in range(len(n)-1):
            code.append((n[i], n[i+1]))
        return code

                   

