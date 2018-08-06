print("此程序只使用了密文对照表中的第二张表，且AB的顺序请自行斟酌")

alphabet = "abcdefghiklmnopqrstuwxyz"

controlTable = [
                "AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB",
                "AABBA","AABBB","ABAAA","ABAAB","ABABA","ABABB",
                "ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB",
                "BAABA","BAABB","BABAA","BABAB","BABBA","BABBB",
               ]

ciphertext = filter(str.isalpha,input("输入要解密的密文:"))

ciphing = ""

for i in ciphertext:

    if i.islower():

        ciphing +='A'

    else:

        ciphing +='B'


print (ciphing)

for i in range(len(ciphing)//5):

    try:
    
        print(alphabet[controlTable.index(ciphing[i*5:i*5+5])],end="")

    except:

        print("*",end="")

print("")
