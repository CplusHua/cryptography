import binascii

def n2s(num):
    #t = hex(num)[2:]            #if python3
    t = hex(num)[2:-1]          #if python2
    if len(t) % 2 == 1:
        t = '0'+ t
    print(t)
    return(binascii.a2b_hex(t).decode('latin1'))

def egcd(a, b):
    if a == 0:
      return (b, 0, 1)
    else:
      g, y, x = egcd(b % a, a)
      return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
      raise Exception('modular inverse does not exist')
    else:
      return x % m

p = 8767867843568934765983476584376578389
q = 3487583947589437589237958723892346254777
e = 65537
d = modinv(e, (p-1)*(q-1))
n = p*q
c = 0x0C6B16AA9B0139542FEEEDD6AE62D6F6498206F133DCFE5F45C139B8776D18DC


m=pow(c,d,n)

print(hex(m))

print(n2s(m))
