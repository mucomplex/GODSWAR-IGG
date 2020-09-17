import os
import sys
from god_crypt import *

data = input("Your data here:")
data = bytes.fromhex(data) 
decrypt = god_decrypt()
print("packet size: %i" % len(data)) 
data = decrypt.run(bytearray(data))
print(data)
new_data = binascii.hexlify(data)
print(new_data)

for i in range(0,len(new_data),2):
    print("0x"+ new_data[i:i+2].decode('UTF-8') +",",end='')
