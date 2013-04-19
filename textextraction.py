def populate(codefile):

    '''(file open for reading) -> list of str

    Read the Opcodes from a portable executable(PE) and return a list where each
    list of Opcodes are arranged next to each other

    Precondition:

    '''

    #skip over the header
    line = codefile.readline()
    
    
    code = []

    for n in codefile :
    	#search for the opcode file and append to code
    	opcode = 0

    	for opcode in n :
    		 

