ciphertext = ""
keytLen = ""
maxLetter = 'E'   # E 是英语里频率最高的字母

def ConveLetter(letter):

    print (chr((ord(letter) - ord(maxLetter))%26 + 97))


def GenAnaly(nowList):

    nowDic = {}

    topLetter = ''

    topNumber = 0

    for i in nowList:          #初始化nowDic字典
        
        nowDic[i] = 0

    for i in nowList:          #统计某密文出现的次数

        nowDic[i] += 1
    
    for i in nowDic:

        if nowDic[i] > topNumber :

            topNumber = nowDic[i]

            topLetter = i

    ConveLetter(topLetter)


def StrSplit():

    for i in range(keytLen):

        print("------------------\nCRACKING position %d = "%(i+1),end='')
        
        GenAnaly(ciphertext[i::keytLen])


def Scanf():

    global ciphertext,keytLen

    string = filter(str.isalpha,input("Please enter ciphertext:").lower())

    for i in string:

        if 97 <= ord(i) <=122:

            ciphertext += i 

    ciphertext = ciphertext.upper()

    keytLen = int(input("Please enter key length:"))

    if type(keytLen) != int:

        print("Key length error!!!")

        sys.exit()


def main():

    Scanf()

    StrSplit()


if "__main__" == __name__:

    main()
