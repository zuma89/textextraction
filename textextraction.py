def populate(codefile):

    '''(file open for reading) -> list of str

    Read the Opcodes from a portable executable(PE) and return a list where each
    list of Opcodes are arranged next to each other

    Precondition:

    '''

    #skip over the header
    line = codefile.readline();
