key = 0
cipher = 'e9e3eee8f4f7bffdd0bebad0fcf6e2e2bcfbfdf6d0eee1ebd0eabbf5f6aeaeaeaeaeaef2'
while key<1000:
	key=key+1
	flag = ""
	for i in range(0,len(cipher),2):
		flag += chr(int(cipher[i:i+2],16) ^ key)
	print(flag)
