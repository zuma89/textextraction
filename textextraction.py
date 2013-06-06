from collections import Counter

def n_gram_opcodes(source, n):
    source = open(source).read()
    OPCODES = set(["mov", "equ", "proc", "neg", "add", "push", "jmp", "dec", "int", "cmp",
                  "call", "or", "pop", "rep", "xor", "out", "in", "db", "sub", "lea", "jne", 
                  "retf", "sub", "sbb", "clc", "xchg", "jb", "dw", "je"])
    
    source_words = source.split()
    opcodes = [w for w in source_words if w in OPCODES]
    
    return Counter(zip(*[opcodes[i:] for i in range(n)]))
