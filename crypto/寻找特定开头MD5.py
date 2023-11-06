import hashlib
def crack(pre):
	for i in range(0, 999999):
		if (hashlib.md5(str(i).encode("UTF-8")).hexdigest())[0:6] == str(pre):
			print(i)
			break
crack("c4d038")