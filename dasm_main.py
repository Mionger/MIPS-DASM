import sys
from dasm_code import Code

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: disassembler input_name output_name")
        exit(1)
    file_input  = sys.argv[1]
    file_output = sys.argv[2]

    # open the machine code file
    machine_code_file = open(file_input, mode='r')
    # open the target file
    mips_code_file = open(file_input, mode='w')

    while True:
        line = machine_code_file.readline()
        if not line:
            break
        
        # ignore basic information of .coe file
        if line == "memory_initialization_radix = 16;memory_initialization_radix = 16;\n" or line == "memory_initialization_vector =\n":
            continue
        
        code = Code(line)
        code.hex_code_to_bin_code()
        code.bin_code_to_mips_code()

        mips_code_file.write(code.mips_code + '\n')
    
    mips_code_file.close()
    machine_code_file.close()
    print("Disassembly over.")