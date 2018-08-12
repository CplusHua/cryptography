###
###    Date:2018-08-11
###   Time:12:33 GMT
###  Author:nianhua
###

class SimpleSub:

    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self,ciphertext = 'QWERTYUIOPASDFGHJKLZXCVBNM'):

        if len(ciphertext) != 26 :

            ciphertext = 'QWERTYUIOPASDFGHJKLZXCVBNM'

        self.ciphertext = ciphertext

    def encipher(self,plaintext):

        afterencry = ''

        for i in plaintext:

            afterencry += self.ciphertext[self.alphabet.index(i)]
    
        return afterencry
    
    def decipher(self,cipher):

        afterencry = ''

        for i in cipher:

            afterencry += self.alphabet[self.ciphertext.index(i)]

        return afterencry


def main():

    newobj = SimpleSub()

    print(newobj.encipher("THESECHATSARETHEPLEASURABLE"))



if "__main__" == __name__:

    main()
