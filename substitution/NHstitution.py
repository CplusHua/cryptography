###
###    Date:2018-08-11
###   Time:12:33 GMT
###  Author:nianhua
###

class SimSubst:

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def __init__(self,ciphertext = 'qwertyuiopasdfghjklzxcvbnm'):

        if len(ciphertext) != 26 :

            ciphertext = 'qwertyuiopasdfghjklzxcvbnm'

        self.ciphertext = ciphertext

    def encode(self,plaintext):

        afterencry = ''

        for i in plaintext:

            afterencry += self.ciphertext[self.alphabet.index(i)]
    
        return afterencry
    
    def uncode(self,cipher):

        afterencry = ''

        for i in cipher:

            afterencry += self.alphabet[self.ciphertext.index(i)]

        return afterencry


def main():

    newobj = SimSubst()

    print(newobj.uncode(newobj.encode("nianhua")))



if "__main__" == __name__:

    main()
