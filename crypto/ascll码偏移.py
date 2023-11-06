string = 'd4e8e1f4a0f7e1f3a0e6e1f3f4a1a0d4e8e5a0e6ece1e7a0e9f3baa0c4c4c3d4c6fbb9b2b2e1e2b9b9b7b4e1b4b7e3e4b3b2b2e3e6b4b3e2b5b0b6b1b0e6e1e5e1b5fd'
flag = ''
for i in range(len(string)/2):
    tmp = int(string[2*i:2*i+2], 16)
    tmp = tmp & 0b01111111
    flag += chr(tmp)
print flag
