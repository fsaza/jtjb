#使用脚本删除空行
with open('a.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
lines = filter(lambda x: x.strip(), lines)
with open('a.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines)
f=open('a.txt','r') 
fi=open('out.txt','w')
while 1:
  a=f.readline().strip() 
  if a:
    if len(a)==16:#键盘流量的话len为16鼠标为8 
      out=''
      for i in range(0,len(a),2):
        if i+2 != len(a):
          out+=a[i]+a[i+1]+":" 
        else:
          out+=a[i]+a[i+1] 
      fi.write(out) 
      fi.write('\n') 
  else: 
    break 
fi.close()
#最后用脚本提取
   # print((line[6:8])) #输出6到8之间的值
   #取出6到8之间的值
mappings = { 0x04:"A",  0x05:"B",  0x06:"C", 0x07:"D", 0x08:"E", 0x09:"F", 0x0A:"G",  0x0B:"H", 0x0C:"I",  0x0D:"J", 0x0E:"K", 0x0F:"L", 0x10:"M", 0x11:"N",0x12:"O",  0x13:"P", 0x14:"Q", 0x15:"R", 0x16:"S", 0x17:"T", 0x18:"U",0x19:"V", 0x1A:"W", 0x1B:"X", 0x1C:"Y", 0x1D:"Z", 0x1E:"1", 0x1F:"2", 0x20:"3", 0x21:"4", 0x22:"5",  0x23:"6", 0x24:"7", 0x25:"8", 0x26:"9", 0x27:"0", 0x28:"\n", 0x2a:"[DEL]",  0X2B:"    ", 0x2C:" ",  0x2D:"-", 0x2E:"=", 0x2F:"[",  0x30:"]",  0x31:"\\", 0x32:"~", 0x33:";",  0x34:"'", 0x36:",",  0x37:"." }
nums = []
keys = open('out.txt')
for line in keys:
    if line[0]!='0' or line[1]!='0' or line[3]!='0' or line[4]!='0' or line[9]!='0' or line[10]!='0' or line[12]!='0' or line[13]!='0' or line[15]!='0' or line[16]!='0' or line[18]!='0' or line[19]!='0' or line[21]!='0' or line[22]!='0':
         continue
    nums.append(int(line[6:8],16)) 
keys.close()
output = ""
for n in nums:
    if n == 0 :
        continue
    if n in mappings:
        output += mappings[n]
    else:
        output += '[unknown]'
print('output :\n' + output)