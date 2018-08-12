###
###    Date:2018-08-12
###   Time:03:33 GMT
###  Author:nianhua
###

from ngram_score import ngram_score
from NHsimple import *
import random

fitness = ngram_score('quadgrams.txt')

ctext = input('请输入要破解的密文:')

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9

parentscore,parentkey = maxscore,maxkey[:]

i = 0
while True:
    i += 1
    random.shuffle(parentkey)
    deciphered = SimpleSub(parentkey).decipher(ctext)
    parentscore = fitness.score(deciphered)
    count = 0
    while count < 1000:
        a = random.randint(0,25)
        b = random.randint(0,25)
        child = parentkey[:]
        child[a],child[b] = child[b],child[a]
        deciphered = SimpleSub(child).decipher(ctext)
        score = fitness.score(deciphered)
        if score > parentscore:
            parentscore = score
            parentkey = child[:]
            count = 0
        count += 1
    if parentscore > maxscore:
        maxscore, maxkey = parentscore, parentkey[:]
        print('\n最好的分数:%lf在第%d轮'%(maxscore,i))
        cc = SimpleSub(maxkey)
        print('\t最合适的密钥:' + ''.join(maxkey))
        print('\t可能的明文:'+cc.decipher(ctext))
