###
###    Date:2018-08-08
###   Time:12:33 GMT
###  Author:nianhua
###

class bacon:

    controlTable = [
                    "AAAAA","AAAAB","AAABA","AAABB","AABAA","AABAB",
                    "AABBA","AABBB","ABAAA","ABAAB","ABABA","ABABB",
                    "ABBAA","ABBAB","ABBBA","ABBBB","BAAAA","BAAAB",
                    "BAABA","BAABB","BABAA","BABAB","BABBA","BABBB",
                   ]

    #初始化函数(默认正常加密表)
    def __init__(self,alphabet = "abcdefghiklmnopqrstuwxyz"):

        self.alphabet = alphabet

    def debacon(self,ciphertext):

        planitext = ""

        for i in range(len(ciphertext)//5):

            try:

                planitext += self.alphabet[self.controlTable.index(ciphertext[i*5:i*5+5])]

            except:

                planitext += '*'

        return planitext


def main():

    newobj = bacon()

    print(newobj.debacon("ABBAAABBABABBBAAXAAA"))



if "__main__" == __name__:

    main()
