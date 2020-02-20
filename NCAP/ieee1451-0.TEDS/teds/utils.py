import struct
    
def hex2dec(code):
    return int( code, 16)


def bin2dec(code):
    return int( code, 2) 


def hex2float(code):
    bins = struct.pack(">i", int( code, 16 ))
    return struct.unpack('>f', bins)[0]

def hex2float2(code):
    bins = ''.join(chr(int(code[x:x+2], 16)) for x in range(0, len(code), 2))
    return struct.unpack('>f', bins)[0]
