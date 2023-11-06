from Crypto.Cipher import AES
import os
import gmpy2
from Crypto.Util.number import *

def main():
    encryped_flag = b'\x8c-\xcd\xde\xa7\xe9\x7f.b\x8aKs\xf1\xba\xc75\xc4d\x13\x07\xac\xa4&\xd6\x91\xfe\xf3\x14\x10|\xf8p'
    xor = 91144196586662942563895769614300232343026691029427747065707381728622849079757
    xor_2 = long_to_bytes(xor)
    key = xor_2[:16]*2
    iv = bytes_to_long(key[16:])^bytes_to_long(xor_2[16:])
    iv = long_to_bytes(iv)
    aes = AES.new(key,AES.MODE_CBC,iv)
    flag = aes.decrypt(encryped_flag)
    print(flag)

    pass
if __name__ == '__main__':
    main()