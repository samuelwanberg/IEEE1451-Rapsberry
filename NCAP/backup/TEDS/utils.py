'''
  Package for utils functions for example convert numbers etc..
'''
def convert_dec_to_bin(number, bits=0):
    '''
      Use example: 
      convert_dec_to_bin(10,5)  => Result: 01010
      convert_dec_to_hex(103,8) => Result:  01100111
    '''
    assert type(number) == int, "Number type don't int"

    binary = bin(number)[2:]
    
    if len(binary) < bits:
       rest = bits - len(binary) 
       return  ("0" * rest) + binary
    else:
        return binary

def  convert_bin_to_hex(binary, octet=1):
    '''OK '''

    '''
      Use example: 
      convert_bin_to_hex(1011,2)  => Result: 0B
      convert_bin_to_hex(100111,2) => Result:  
    '''
    assert type(binary) == str, "Binary type don't str"

    #verificar se existe apenas 0 ou 1 na string binaria
    verify = map( lambda b: False if not b in ["0","1"]
                  else True, binary)
    assert not False in list(verify), "Value of binary Number is incorrect "

    assert octet > 0, "oct is less than 1"
    
    bits = 8 * octet

    if len(binary) < bits:
        rest = bits - len(binary)
    else:
        rest = 0

    binary =  "0" * rest  + binary
    
    hexcode = []
    for i in range(0, len(binary), 4):
        hexcode.append( "{0:0>1X}".format(int(binary[i:i+4], 2))  )

    _format = ""
    for i in range(0, len(hexcode) ,2):
        _format = _format + "".join(hexcode[i:i+2]) + " " 
        
    return _format
       
def convert_dec_to_hex(number, oct=1):

    '''
      Use example: 
      convert_dec_to_hex(10,2)  => Result: 00 0A
      convert_dec_to_hex(103,3) => Result: 00 00 67
      Update  
    '''
    assert type(number) == int, "Number type don't int"
    hexcode = "{" + "0:0>{}X".format(2*oct) + "}"
    hexcode = list(hexcode.format(number))

    return " ".join( [ "".join( hexcode[i:i+2] )  for i in range(0, len(hexcode), 2) ] ) 

def convert_float_to_hex(number , oct=1):
    
    '''
      Use example: 
      convert_float_to_hex(0.5,2)  => Result: 0A
      convert_float_to_hex(1.0,3)  => Result:  067
    '''
    assert type(number) == float, "Number type don't float"

    import bitstring

    binary = bitstring.BitArray(float = number, length=32)
    hexcode = convert_bin_to_hex(binary.bin, oct=4)

    return hexcode   


def UInt32(number):

    """
    Class number size 4 octect
    representive positive number from 0 to 4294967296
    """

    assert number >= 0 and number <= 4294967296, "Class Number is not  UInt32"

    return convert_dec_to_hex(number, 4)

def UInt8(number):

    """
    Class number size 1 octect
    representive positive number from 0 to 255
    """

    assert number >= 0 and number <= 255, "Class Number is not  UInt8"

    return convert_dec_to_hex(number, 1)

def Uint16(number):

    """
    Class number size 2 octect
    representive positive number from 0 to 65536
    """

    assert number >= 0 and number <= 65536, "Class Number is not  UInt8"

    return convert_dec_to_hex(number, 2)


def Float32():
    pass
