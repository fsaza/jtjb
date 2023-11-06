from gmpy2 import *
import libnum
import hashlib
n = 201354090531918389422241515534761536573
c = 20442989381348880630046435751193745753
p = 13934102561950901579
q = 14450452739004884887
e = 2
inv_p = invert(p, q)
inv_q = invert(q, p)
mp = pow(c, (p + 1) // 4, p)
mq = pow(c, (q + 1) // 4, q)
a = (inv_p * p * mq + inv_q * q * mp) % n
b = n - int(a)
c = (inv_p * p * mq - inv_q * q * mp) % n
d = n - int(c)
#因为rabin 加密有四种结果，全部列出。
aa=[a,b,c,d]
for i in aa:
    print(i)
    print(libnum.n2s(int(i))) 
