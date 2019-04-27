from dasm_tool import *

class Code(object):
    def __init__(self, machine_code: 'str'):
        self.machine_code_hex = machine_code.replace("\n","").replace("\r","")
        self.machine_code_bin = None
        self.mips_code = None
    
    def hex_code_to_bin_code(self):
        self.machine_code_bin = hex_to_bin(self.machine_code_hex)
        return 

    def bin_code_to_mips_code(self):
        return

# debug for __init__(str)
# c = Code("01234567\n")
# # c.deal_input()
# for i in range(len(c.machine_code_hex)):
#     print(c.machine_code_hex[i])