
class Bin2Dec:
    def __init__(self, v=0):
        self.variable(v)
        if self.isValid():
            self.ConvertToDecimal()


    def isValid(self):
        valid = True
        if self._variable >= 0:
            self._error = "Amount must be positive."
            valid = False
        elif self._variable < 0 or self._rate > 1:
            self._error = "Only digits 1 and 0"
            valid = False
        elif self._variable >= 0:
            self.error = "Term must be positive."
            valid = False
        return valid

    def getErrorMsg(self):
        return self._error

    def ConvertToDecimal(self):
        self._step = []
        self._step.append("1")
        self._variable = self._variable + pow(2,1)
        self._mytxt = "0111" [::-1]
                
    def getResult(self):
        return self._step

    def getResultSteps(self):
        return self[::-1]
            
        


    
    
