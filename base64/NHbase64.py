###
###    Date:2018-08-07
###   Time:12:33 GMT
###  Author:nianhua
###

class base64:

    #初始化函数(默认正常加密表)
    def __init__(self,alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"):

        self.alphabet = alphabet
    
    def _EnInsideManage(self,strlist):
    
        strflag = ""

        temp = ord(strlist[0]) >> 2

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[0])&3)<<4)|(ord(strlist[1])>>4)

        strflag += self.alphabet[temp]

        temp = ((ord(strlist[1])&15)<<2)|(ord(strlist[2])>>6)

        strflag += self.alphabet[temp]

        temp = (ord(strlist[2])&63)

        strflag += self.alphabet[temp]
    
        return strflag

    def enbase64(self,charString):

    
        encode = ""

        for i in range(len(charString)//3):

            encode += self._EnInsideManage(charString[i*3:i*3+3])

        if len(charString)%3!=0:

            if len(charString)%3 == 1:

                encode += self._EnInsideManage(charString[-1:]+chr(0)+chr(0))[:2]+"=="

            if len(charString)%3 == 2:

                encode += self._EnInsideManage(charString[-2:]+chr(0))[:3]+'='

        return encode

    def TenToBin(self,tenum):

        binstr = ""

        for i in range(5,-1,-1):

            if 1 == (tenum//(2**i)):

                binstr += '1'

                tenum = tenum%(2**i)

            else:

                binstr += '0'

        return binstr

    def BinToStr(self,strbin):
        "Turn the binary string to a ASCII string"

        strten = ""
    
        for i in range(len(strbin)//8):

            num = 0

            test = strbin[i*8:i*8+8]

            for j in range(8):

                num += int(test[j])*(2**(7-j))

            strten += chr(num)

        return strten

    def debase64(self,base64string):

        binstr = ""

        for i in base64string:

            binstr += self.TenToBin(self.alphabet.find(i))

        return self.BinToStr(binstr)

def main():

    newobj = base64("qazwsxedcrfvtgbyhnujmikolpQAZWSXEDCRFVTGBYHNUJMIKOLP-|0987654321")

    print(newobj.debase64(newobj.enbase64("nianhua")))

if "__main__" == __name__:

    main()

