import gmpy2
import libnum
from Crypto.Util.number import *
from binascii import a2b_hex, b2a_hex

flag = "*****************"

p = 262248800182277040650192055439906580479
q = 262854994239322828547925595487519915551
c = 27565231154623519221597938803435789010285480123476977081867877272451638645710
e = 65533
n = p * q
phi = (p - 1) * (q - 1)
d = gmpy2.invert(e, phi)
m = pow(c, d, n)
print(libnum.n2s(int(m)))