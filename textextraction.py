from collections import Counter

def n_gram_opcodes(source, n):
    source = open(source).read()
    OPCODES = set(["aaa","aad","aas","adc","add","and","arpl","bound","bsf","bsr","bswap","bt",
    			  "btc","btr","bts","call","cbw","cdq","mov", "equ", "proc", "neg","cld", "cli",
    			  "push", "or", "pop", "rep", "xor", "out", "in", "db", "daa","das","dec","div",
    			  "enter","esc","hlt","idiv","imul","inc","ins","into","invd","invlpg","iret",
    			  "ja","jae","jb","jbe","jc","jcxz","je","jg","jge","jl","jle","jnc","jno","jns",
    			  "jnp","jo","jp","js","lahf","lar","lds","leave","les","lfs","lgdt","lidt","lgs",
    			  "lldt","lmsw","lock","lods","loop","loope","loopnz","lsl","lss","ltr","movs",
    			  "movsx","movzx","mul","neg","nop","not","outs","popa","popf","pusha","pushf",
    			  "rcl","rcr","rep","repe","repne","ret","rol","ror","sahf","sal","sbb","scas",
    			  "setae","setb","setbe","sete","setne","setl","setge","setle","setg","sets",
    			  "setns","setc","setnc","seto","setno","setp","setnp","sgdt","sidt","shr","shld",
    			  "sldt","smsw","stc,","std","sti","stos","str","sub","test","verr","verw","wait",
    			  "jmp","clts","cmc","cmps","cmpxchg","cwd","cwde", "int", "cmp","call", "wbinvd",
    			  "sub", "lea", "jne","retf", "sub", "sbb", "clc", "xchg", "dw","xlat"])
    
    source_words = source.split()
    opcodes = [w for w in source_words if w in OPCODES]
    
    return Counter(zip(*[opcodes[i:] for i in range(n)]))
