from z3 import *

outBin = '01111111001101111011010110100110100111001011110011100101000000000'

def numcc(keytLen):

    p0,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,p22,p23,p24,p25,p26,p27,p28,p29,p30,p31,p32,p33,p34,p35,p36,p37,p38,p39 = Ints('p0 p1 p2 p3 p4 p5 p6 p7 p8 p9 p10 p11 p12 p13 p14 p15 p16 p17 p18 p19 p20 p21 p22 p23 p24 p25 p26 p27 p28 p29 p30 p31 p32 p33 p34 p35 p36 p37 p38 p39')

    s = Solver()

    for i in range(keytLen):

        ceshi =  outBin[i:keytLen+i+1]

        ming = ''

        for i in range(keytLen):

            if ceshi[i] == '1':
            
                ming += 'p' + str(i) + '+'

            else:

                pass
    
        ming = ming[0:-1] + '==' + str(ceshi[-1])
        #print ming    
        s.add(eval(ming))
    if s.check() == sat:
        print keytLen
        print s.model()

    #print s.check()

for i in range(2,30):

    numcc(i)
    #pass
#numcc(14)
