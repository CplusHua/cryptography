###
###    Date:2018-08-24
###   Time:09:00 GMT
###  Author:nianhua
###

from ngram_score import *

fitness = ngram_score('quadgrams.txt')
alphabetb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
scoretmp = []
newliste = []
ciphertext = input("请输入要破解的密码:")

def caser(i):

    plaintext =""

    for j in ciphertext:
        
        if 64 < ord(j) < 91:
        
            plaintext += alphabetb[alphabetb.find(j)-i-1]
        
        elif 96 < ord(j) <123:

            plaintext += alphabets[alphabets.find(j)-i-1]

        else:

            plaintext += j
    

    return plaintext

def main():

    for i in range(26):

        scoretmp.append([])

        plaintext = caser(i) 


        scoretmp[i].append(i)
        scoretmp[i].append(plaintext)
        scoretmp[i].append(fitness.score(''.join(list(filter(str.isalpha,plaintext))).upper()))

    for i in range(26):

        scorevi = -99e9
        goodvi = 0

        for j in scoretmp:

            if j[2] > scorevi:

                scorevi = j[2]
                goodvi = j[0]

        newliste.append(scoretmp[goodvi][:])

        scoretmp[goodvi][2] = -99e9

        print("%2d:%4.2f:%s"%(newliste[i][0],newliste[i][2],newliste[i][1]))


if "__main__" == __name__:

    main()
