#Loan

class Loan:

    def __init__(self,a=0.0,r=0.0,t=0):
        #create 'private' variables for the class values
        self.setAmt(a)
        self.setRate(r)
        self.setTerm(t)
        self._error = ""
        if self.isValid():
            self.buildLoan()
        
        
           
    #set and get methods 'encapsulate' data values
    def setAmt(self,value):
        self._amt = value
    def getAmt(self):
        return self._amt   
    def setRate(self,value):
        self._rate = value
    def getRate(self):
        return self._rate
    def setTerm(self,value):
        self._term = value
    def getTerm(self):
        return self._term

    def isValid(self):
        valid = True
        if self._amt <= 0:
            self._error = "Amount must be positive."
            valid = False
        elif self._rate < 1 or self._rate > 25:
            self._error = "Rate out of bounds: 1 to 25 only"
            valid = False
        elif self._term <= 0:
            self.error = "Term must be positive."
            valid = False
        return valid

    def getError(self):
        return self._error
    
    def buildLoan(self):
        self._bbal = [0.0] * self._term
        self._intChg = [0.0] * self._term
        self._ebal = [0.0] * self._term
        
        morate = self._rate/12.0/100.0
        denom = ((1+morate) ** self._term) - 1
        self._mopmt = (morate + morate/denom) * self._amt
        self._bbal[0] = self._amt
        for i in range(0, self._term):
            if i > 0:
                self._bbal[i] = self._ebal[i-1]
            self._intChg[i] = self._bbal[i] * morate
            self._ebal[i] = self._bbal[i] + self._intChg[i] - self._mopmt


                
    def getMoPmt(self):
        return self._mopmt
    def getInterest(self):
        return (self._mopmt * self._term) - self._amt 
    def getBegBal(self, mo):
        return self._bbal[mo-1]
    def getIntChg(self, mo):
        return self._intChg[mo-1]
    def getEndBal(self, mo):
        return self._ebal[mo-1]








            
            
    






        
