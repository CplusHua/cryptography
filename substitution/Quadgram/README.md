###
###    Date:2018-08-12
###   Time:03:33 GMT
###  Author:nianhua
###

需要注意的是这些都是适用于python3的程序</br>


````
from pycipher import SimpleSubstitution as SimpleSub  #导入cipher模块
import random                                         #导入随机模块
import re                                             #导入re模块
from ngram_score import ngram_score                   #导入评分模块
fitness = ngram_score('quadgrams.txt') # load our quadgram statistics

ctext='pmpafxaikkitprdsikcplifhwceigixkirradfeirdgkipgigudkcekiigpwrpucikceiginasikwduearrxiiqepcceindgmieinpwdfprduppcedoikiqiasafmfddfipfgmdafmfdteiki'
ctext = re.sub('[^A-Z]','',ctext.upper())            #密文转换为大写

maxkey = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
maxscore = -99e9
parentscore,parentkey = maxscore,maxkey[:]
print "Substitution Cipher solver, you may have to wait several iterations"
print "for the correct result. Press ctrl+c to exit program."
# keep going until we are killed by the user
i = 0
while 1:
    i = i+1
    random.shuffle(parentkey)                        #将parentkey打乱顺序
    deciphered = SimpleSub(parentkey).decipher(ctext)#使用刚刚的密钥解密
    parentscore = fitness.score(deciphered)          #计算分数
    count = 0                                        #计算器清零
    while count < 1000:                              #至多循环一千次
        a = random.randint(0,25)                     #随机选择一个数
        b = random.randint(0,25)                     #随机选择另一个
        child = parentkey[:]                         
        # swap two characters in the child
        child[a],child[b] = child[b],child[a]        #交换子密钥任意两位
        deciphered = SimpleSub(child).decipher(ctext)#解密
        score = fitness.score(deciphered)            #计算得分
        # if the child was better, replace the parent with it
        if score > parentscore:                      #比较子密钥和父密钥得分，如果子密钥得分高
            parentscore = score                      #则使用子分数代替父分数
            parentkey = child[:]                     #使用子密钥代替父密钥
            count = 0                                #清除计数器
        count = count+1                              #计数器计数
    # keep track of best score seen so far
    if parentscore>maxscore:                         #当尝试超过一千次都没有得到一个子分数大于父分数
        maxscore,maxkey = parentscore,parentkey[:]   #并且分数需要大于一个很低的分数（省的是假的）
        print '\nbest score so far:',maxscore,'on iteration',i
        ss = SimpleSub(maxkey)
        print '    best key: '+''.join(maxkey)
        print '    plaintext: '+ss.decipher(ctext)

````
