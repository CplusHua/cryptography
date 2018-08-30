class LFSR:

    def __init__(self,keyt,feedpath):

        self.trigger  = []
        
        self.feedback = []

        self.degree   = len(keyt)

        self.feed     = len(feedpath)

        if len(feedpath) != self.degree:
        
            return None

        for i in keyt:

            self.trigger.append(i)

        for i in feedpath:

            self.feedback.append(i)
    
    def binxor(self,bin1,bin2):

        if bin1 == bin2:

            return '0'
        
        else:

            return '1'
        
    def getfeed(self):

        self.realdback = []

        for i in range(self.feed):

            if self.feedback[i] == '1':

                self.realdback.append(self.trigger[i])

        for i in range(1,len(self.realdback)):

            self.realdback[0] = self.binxor(self.realdback[0],self.realdback[i])

        return self.realdback[0]

    def tick(self):

        outpin = self.trigger[-1]

        feedpin = self.getfeed()
        
        for i in range(self.degree-1,0,-1):

            self.trigger[i] = self.trigger[i-1]
        
        self.trigger[0] = feedpin

        return outpin
        

if '__main__' == __name__:

    newobj = LFSR('11111111','00011011')

    for i in range(100):

        print(newobj.tick(),end='')
