bit_weight = 32
dict_h_to_b = {
    "0" : "0000",
    "1" : "0001",
    "2" : "0010",
    "3" : "0011",
    "4" : "0100",
    "5" : "0101",
    "6" : "0110",
    "7" : "0111",
    "8" : "1000",
    "9" : "1001",
    "a" : "1010",
    "b" : "1011",
    "c" : "1100",
    "d" : "1101",
    "e" : "1110",
    "f" : "1111"
}

def hex_to_bin(hex_num:'str') -> 'str':
    i = 0
    bin_code = ""
    for i in range(bit_weight // 4):
        bin_code += dict_h_to_b[hex_num[i]]
    return bin_code


def bin_to_hex(bin_num:'str', flag:'bool') -> 'str':
    return ""

def bin_to_dec(bin_num:'str') -> 'str':
    return ""

# debug for hex_to_bin(str)
# print(hex_to_bin("01234567"))
# print(hex_to_bin("89abcdef"))
