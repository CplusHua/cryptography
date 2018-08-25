###
###    Date:2018-08-25
###   Time:09:00 GMT
###  Author:nianhua
###

from ngram_score import *

fitness = ngram_score('quadgrams.txt')
alphabetb = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabets = "abcdefghijklmnopqrstuvwxyz"
score = []
goodscore = -99e9
goodvi = 0
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



for i in range(1,26):

    plaintext = caser(i) 
    
    score.append(fitness.score(''.join(list(filter(str.isalpha,plaintext))).upper()))
    
    print("%2d:%s"%(i,plaintext))

for i in range(25):

    if score[i] > goodscore :

        goodscore = score[i]

        goodvi = i+1

print("最好的明文:%s"%caser(goodvi))
