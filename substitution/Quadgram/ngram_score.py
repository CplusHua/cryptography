'''
使用N-gram概率对文本进行评分
18/08/12
'''
from math import log10

class ngram_score(object):
    def __init__(self,ngramfile,sep=' '):
        ''' 加载包含NCG和计数的文件，计算lg概率 '''
        self.ngrams = {}
        fr = open(ngramfile,'r')
        for line in fr:
            key,count = line.split(sep) 
            self.ngrams[key] = int(count)
        fr.close()
        self.L = len(key)                  #长度：几元组? --> 一般推荐使用四元组
        self.N = sum(self.ngrams.values()) #计算所有四元组次数总和 
        #计算对数概率
        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key])/self.N)  #使用lg(key次数/总次数) 替代 key次数
        self.floor = log10(0.01/self.N)  #不是很理解

    def score(self,text):
        ''' 计算文本得分 '''
        score = 0
        ngrams = self.ngrams.__getitem__       #ngrams变量指向getitem方法
        for i in range(len(text)-self.L+1):    #循环text-3次
            if text[i:i+self.L] in self.ngrams: score += ngrams(text[i:i+self.L])  #判断当前四元组是否存在于字典，如果是则加上lg
            else: score += self.floor                         #如果不存在则加上默认floor
        return score
