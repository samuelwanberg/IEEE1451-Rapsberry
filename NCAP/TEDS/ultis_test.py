from utils import *

def test_convert_bin_to_hex(test, octet=1,  result  ):
    
    assert convert_bin_to_hex(test, octet,) == result, "Test Fail {0} != {1}".format(convert_bin_to_hex(test, octet), result)
    
    print("test_convert_bin_to_hex pass -> ok")





if __name__ == '__main__':
    
    test_convert_bin_to_hex('11101', '1D' )
