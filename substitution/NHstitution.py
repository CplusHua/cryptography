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



def main():

    newobj = SimSubst()

    print(newobj.encode("abcd"))



if "__main__" == __name__:

    main()
