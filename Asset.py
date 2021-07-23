
#Annuity

class Asset:

    def __init__(self,c=0.0,s=0.0,l=0):
        #create 'private' variables for the class values
        self.setCost(c)
        self.setSalvage(s)
        self.setLife(l)
        self._error = ""
        if self.isValid():
            self.buildAsset()
        
        
           
    #set and get methods 'encapsulate' data values
    def setCost(self,value):
        self._cost = value
    def getCost(self):
        return self._cost  
    def setSalvage(self,value):
        self._salvage = value
    def getSalvage(self):
        return self._salvage
    def setLife(self,value):
        self._life = value
    def getLife(self):
        return self._life

    def isValid(self):
        valid = True
        if self._cost <= 0:
            self._error = "Asset must be positive."
            valid = False
        elif self._salvage < 0 or self._cost < self._salvage:
            self._error = "Salvage must be less than cost"
            valid = False
        elif self._life <=0:
            self._error = "Life must be positive."
            valid = False
        return valid

    def getError(self):
        return self._error
    
    def buildAsset(self):
        self._bval = [0.0] * self._life
        self._dep = [0.0] * self._life
        self._eval = [0.0] * self._life
        
        self._bval[0] = self._cost
        self._eval[0] = self._salvage
        
        for i in range(0,self._life):
            if i > 0:
                self._bval[i] = self._eval[i-1]
            self._dep[i] = (self._bval[i] - self._eval[i]) / self._life
            self._eval[i] = self._bval[i] - self._dep[i]
            
            
    def getDepreciation(self):
        return (self._cost - self._salvage) / self._life 
    def getBegVal(self,mo):
        return self._bval[mo-1]
    def getEndVal(self,mo):
        return self._eval[mo-1]






    
    

