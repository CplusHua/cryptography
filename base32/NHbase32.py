###
###    Date:2018-08-06
###   Time:12:33 GMT
###  Author:nianhua
###

class base32:

    #初始化函数(默认正常加密表)
    def __init__(self,alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"):

        self.alphabet = alphabet

    #一次只能处理五个字母
    def _EnInsideManage(self,strlist):

        strflag = ""

        temp = ord(strlist[0])>>3

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[0])&7)<<2)|(ord(strlist[1])>>6)

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[1])&62)>>1)

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[1])&1)<<4)|(ord(strlist[2])>>4)

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[2])&15)<<1)|(ord(strlist[3])>>7)

        strflag += self.alphabet[temp]

        temp = (ord(strlist[3])&124)>>2
    
        strflag += self.alphabet[temp]

        temp = ((ord(strlist[3])&3)<<3)|((ord(strlist[4])&224)>>5)

        strflag += self.alphabet[temp]

        temp = ord(strlist[4])&31

        strflag += self.alphabet[temp]
    
        return strflag    
    
    #加密函数
    def enbase32(self,charString):

        encode = ""
        
        for i in range(len(charString)//5):

            encode +=self. _EnInsideManage(charString[i*5:i*5+5])

        if len(charString)%5!=0:

            if len(charString)%5 == 1:

                encode += self._EnInsideManage(charString[-1:]+chr(0)+chr(0)+chr(0)+chr(0))[:2]+"======"

            if len(charString)%5 == 2:

                encode += self._EnInsideManage(charString[-2:]+chr(0)+chr(0)+chr(0))[:4]+"===="

            if len(charString)%5 == 3:

                encode += self._EnInsideManage(charString[-3:]+chr(0)+chr(0))[:5]+"==="

            if len(charString)%5 == 4:

                encode += self._EnInsideManage(charString[-4:]+chr(0))[:7]+'='

        return encode


    def _TenToBin(self,tenum):

        binstr = ""

        for i in range(4,-1,-1):

            if 1 == (tenum//(2**i)):

                binstr += '1'

                tenum = tenum%(2**i)

            else:

                binstr += '0'

        return binstr

    def _BinToStr(self,strbin):
        "Turn the binary string to a ASCII string"

        strten = ""
    
        for i in range(len(strbin)//8):

            num = 0

            test = strbin[i*8:i*8+8]

            for j in range(8):

                num += int(test[j])*(2**(7-j))

            strten += chr(num)

        return strten

    #解密函数
    def debase32(self,ciphertext):

        binstr = ""
        
        for i in ciphertext:

            binstr += self._TenToBin(self.alphabet.find(i))

        return(self._BinToStr(binstr))


def main():

    newobj = base32("1234567890abcefghijklmnoprstuvwx")

    print(newobj.enbase32("1233123"))

    print(newobj.debase32(newobj.enbase32("1233123")))


if "__main__" == __name__:

    main()
