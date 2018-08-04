#转载请注明出处哦~~~~
#https://github.com/nian-hua/

import operator

alphabet = "abcdefghijklmnopqrstuvwxyz"

ciphertext = ""

keytLen = 0

fridnum = {                         #英文字母出现概率表
        'a':0.08167,'b':0.01492,'c':0.02782,'d':0.04253,
        'e':0.12702,'f':0.02228,'g':0.02015,'h':0.06094,
        'i':0.06966,'j':0.00153,'k':0.00772,'l':0.04025,
        'm':0.02406,'n':0.06749,'o':0.07507,'p':0.01929,
        'q':0.00095,'r':0.05987,'s':0.06327,'t':0.09056,
        'u':0.02758,'v':0.00978,'w':0.02360,'x':0.00150,
        'y':0.01974,'z':0.00074,
        }

def ReturnPositiveNum(num):

    if num >= 0 :

        return num

    if num < 0 :

        return 0-num


def getkey(nowDic,nowlen):                                             #这函数写的有点复杂，我自己都特么看不懂了。。尴尬

    print("------------------------------")

    print(nowDic)                                                      #打印一下当前密文字典

    print("------------------------------")
    
    alphdic = {}

    machtmp = []

    for i in fridnum:                                                  #根据密文长度，统计出明文应该出现的次数

        alphdic[i] = round(fridnum[i] * nowlen)

    print(alphdic)                                                     #打印一下明文各字母应该出现的次数
                                                                       #虽然每次循环都一样
    print("-----------------------------")

    #    比较核心的for循环
        
    for i in range(3,int(nowlen*fridnum['e'])+1):                       #只循环字母出现次数在3~Max

        for  j in nowDic:

            if (i-2)<=nowDic[j]<=(i+2):

                for k in alphdic:

                    if (i-2)<=alphdic[k]<=(i+2):

                       machtmp.append(ReturnPositiveNum(ord(j)-ord(k)))          #将猜测的密钥加入列表

    newmachdic = {}

    for i in machtmp:

        newmachdic[i] = 0

    for i in machtmp:

        newmachdic[i] += 1 

    newmachdic_t = sorted(newmachdic.items(),key=operator.itemgetter(1),reverse = True)   #重新统计

    print("因子:次数")

    count_dic = 0

    for i,j in newmachdic_t:

        print("%3c:%3d"%(alphabet[i],j))

        count_dic += 1

        if count_dic >= 5:

            break


def FreqAnaly(nowList): 
    
    nowDic = {}

    for i in nowList:          #初始化nowDic字典
        
        nowDic[i] = 0

    for i in nowList:          #统计某密文出现的次数

        nowDic[i] += 1
    
    for i in nowDic:           #打印出统计频率look look

        print("%s:%s"%(i,nowDic[i]*'█'))

    getkey(nowDic,len(nowList)) 

    #print(nowDic)


def StrSplit():

    for i in range(keytLen):
 
        FreqAnaly(ciphertext[i::keytLen]) #使用FreqAnaly函数处理每个密文分量
        
        print("----------")


def Scanf():

    global ciphertext,keytLen

    ciphertext = input("请输入密文:")

    keytLen = int(input("请输入密钥长度:"))


def main():

    Scanf()

    StrSplit()


if "__main__" == __name__:

    main()
