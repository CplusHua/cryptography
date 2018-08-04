#转载请注明出处哦~~~~
#https://github.com/nian-hua/
ciphertext = ""


def Scanf():
   
    global ciphertext

    ciphertext = input("请输入密文:")

    ciphertext.lower()

def friedman(ciphLen):  

    for i in range(ciphLen):           #此密钥分量位置

        alphabet = {}

        countnum = 0

        text = ciphertext[i::ciphLen] #取出密钥此密钥分量对应的密文部分
        
        for i in text:                #初始化alphabet数组

            alphabet[i] = 0


        for i in text:

            alphabet[i] += 1
        
        for i in alphabet:             #计算重合因子指数

            countnum += alphabet[i] * (alphabet[i] - 1)

        coincidence = float(countnum)/(len(text)*(len(text)-1))

        print (coincidence)


def main():

    Scanf()  #接收程序输入

    for i in range(10):   #猜测密钥的长度大概是多少，例如这个就是1~10

        friedman(i)
        
        print("------------------------------")




if "__main__" == __name__ :

    main()
