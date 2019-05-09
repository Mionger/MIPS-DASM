from dasm_tool import hex_to_bin
from dasm_tool import bin_to_hex
from dasm_tool import addr_bin_to_hex

dict_reg = {
    "00000" : "$0 ",
    "00001" : "$1 ",
    "00010" : "$2 ",
    "00011" : "$3 ",
    "00100" : "$4 ",
    "00101" : "$5 ",
    "00110" : "$6 ",
    "00111" : "$7 ",
    "01000" : "$8 ",
    "01001" : "$9 ",
    "01010" : "$10",
    "01011" : "$11",
    "01100" : "$12",
    "01101" : "$13",
    "01110" : "$14",
    "01111" : "$15",
    "10000" : "$16",
    "10001" : "$17",
    "10010" : "$18",
    "10011" : "$19",
    "10100" : "$20",
    "10101" : "$21",
    "10110" : "$22",
    "10111" : "$23",
    "11000" : "$24",
    "11001" : "$25",
    "11010" : "$26",
    "11011" : "$27",
    "11100" : "$28",
    "11101" : "$29",
    "11110" : "$30",
    "11111" : "$31"
}

class Code(object):
    def __init__(self, machine_code: 'str'):
        self.machine_code_hex = machine_code.replace("\n","").replace("\r","")
        self.machine_code_bin = None
        self.mips_code = None
    
    def hex_code_to_bin_code(self):
        self.machine_code_bin = hex_to_bin(self.machine_code_hex) 

    def bin_code_to_mips_code(self):
        op = self.machine_code_bin[0:6]
        rs = self.machine_code_bin[6:11]
        rt = self.machine_code_bin[11:16]
        rd = self.machine_code_bin[16:21]
        sa = self.machine_code_bin[21:26]
        func = self.machine_code_bin[26:32]
        imme = self.machine_code_bin[16:32]
        addr = self.machine_code_bin[6:32]
        
        if op == "000000":
            self.mips_code = self.op_0000(rs, rt, rd, sa, func)
        if op == "001000":
            self.mips_code = self.addi(rs, rt, imme)
        if op == "001001":
            self.mips_code = self.addiu(rs, rt, imme)
        if op == "001100":
            self.mips_code = self.andi(rs, rt, imme)
        if op == "001101":
            self.mips_code = self.ori(rs, rt, imme)
        if op == "001110":
            self.mips_code = self.xori(rs, rt, imme)
        if op == "001111":
            self.mips_code = self.lui(rs, rt, imme)
        # beq and bne cant restore the lables
        if op == "000100":
            self.mips_code = self.beq(rs, rt, imme)
        if op == "000101":
            self.mips_code = self.bne(rs, rt, imme)
        if op == "001010":
            self.mips_code = self.slti(rs, rt, imme)
        if op == "001011":
            self.mips_code = self.sltiu(rs, rt, imme)
        if op == "100011":
            self.mips_code = self.lw(rs, rt, imme)
        if op == "101011":
            self.mips_code = self.sw(rs, rt, imme)
        if op == "000010":
            self.mips_code = self.j(addr)
        if op == "000011":
            self.mips_code = self.jal(addr)

    def op_0000(self, rs:'str', rt:'str', rd:'str', shamt:'str', func:'str'):
        # 顺序为dst
        if func == "100000":
            return ("add     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100001":
            return ("addu    "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100010":
            return ("sub     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100011":
            return ("subu    "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100100":
            return ("and     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100101":
            return ("or      "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100110":
            return ("xor     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "100111":
            return ("nor     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "101010":
            return ("slt     "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "101011":
            return ("sltu    "+dict_reg[rd]+","+dict_reg[rs]+","+dict_reg[rt])
        if func == "000100":
            return ("sllv    "+dict_reg[rd]+","+dict_reg[rt]+","+dict_reg[rs])
        if func== "000110":
            return ("srlv    "+dict_reg[rd]+","+dict_reg[rt]+","+dict_reg[rs])
        if func== "000111":
            return ("srav    "+dict_reg[rd]+","+dict_reg[rt]+","+dict_reg[rs])
        if func == "000000":
            return ("sll     "+dict_reg[rd]+","+dict_reg[rt]+","+bin_to_hex(shamt, 32, 0))
        if func == "000010":
            return ("srl     "+dict_reg[rd]+","+dict_reg[rt]+","+bin_to_hex(shamt, 32, 0))
        if func == "000011":
            return ("sra     "+dict_reg[rd]+","+dict_reg[rt]+","+bin_to_hex(shamt, 32, 0))
        if func == "001000":
            return ("jr      "+dict_reg[rs])

    def addi(self, rs:'str', rt:'str', imme:'str'):
        return ("addi    "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 1))

    def addiu(self, rs:'str', rt:'str', imme:'str'):
        return ("addiu   "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 1))
    
    def andi(self, rs:'str', rt:'str', imme:'str'):
        return ("andi    "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 0))
    
    def ori(self, rs:'str', rt:'str', imme:'str'):
        return ("ori     "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 0))

    def xori(self, rs:'str', rt:'str', imme:'str'):
        return ("xori    "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 0))

    def lui(self, rs:'str', rt:'str', imme:'str'):
        return ("lui     "+dict_reg[rt]+","+bin_to_hex(imme, 32, 0))

    def beq(self, rs:'str', rt:'str', imme:'str'):
        return ("beq     "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 1))

    def bne(self, rs:'str', rt:'str', imme:'str'):
        return ("bne     "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 1))
    
    def slti(self, rs:'str', rt:'str', imme:'str'):
        return ("slti    "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 1))

    def sltiu(self, rs:'str', rt:'str', imme:'str'):
        return ("sltiu   "+dict_reg[rs]+","+dict_reg[rt]+","+bin_to_hex(imme, 32, 0))

    def lw(self, rs:'str', rt:'str', imme:'str'):
        return ("lw      "+dict_reg[rt]+","+bin_to_hex(imme, 32, 1)+"("+dict_reg[rs]+")")

    def sw(self, rs:'str', rt:'str', imme:'str'):
        return ("sw      "+dict_reg[rt]+","+bin_to_hex(imme, 32, 1)+"("+dict_reg[rs]+")")

    def j(self, addr:'str'):
        return ("j       "+addr_bin_to_hex(addr))

    def jal(self, addr:'str'):
        return ("jal     "+addr_bin_to_hex(addr))
