from collections import Counter

def n_gram_opcodes(source, n):
    source = open(source).read()
    OPCODES = set(["add","call","cmp","mov","jnz","jmp","jz","lea","pop","push",
        "retn","sub","test","xor"])
    
    source_words = source.split()
    opcodes = [w for w in source_words if w in OPCODES]
    
    return Counter(zip(*[opcodes[i:] for i in range(n)]))
