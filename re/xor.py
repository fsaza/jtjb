s=[xxx]
v1=1
v2=0x3
for i in range(len(s)):
	print(chr(s[i]-v1^v2),end="")# ^号运算符优先级低于减号