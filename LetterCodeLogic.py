#LetterCodeLogic module Meri Iskali
# 'business' object class for LetterCode operations...

class LCL:
    """Encode/Decoden Functions"""

    @staticmethod
    def Decode(msg):
        #separate numbers from msg string (e.g., "1,2,3")
        nums = msg.split(",") #produces a list of separate items
        result = ""
        for x in nums:
            try:
                n = int(x.strip()) #remove leading/trailling spaces...
                if n == 0:
                    c = " "
                elif n < 0 or n > 26:
                    c = "?"
                else:
                    #ASCII scheme has A=65, B=66, etc.
                    c = chr(n+64)
            except ValueError:
                c = "?"

            result += c  #same as: result = result + c
        
        return result


    @staticmethod
    def Encode(msg):
        m = msg.upper()
        result = ""
        for i in range(0,len(m)):
            x = ord(m[i])
            if x == 32:
                x = 0
            else:
                x = x - 64
                if x < 1 or x > 26:
                    x = 99
            result = result + str(x) + " "
        return result
                    
            
        #must be sure msg is all caps
        #must process each character of the string up to length
        #   "ABC": A => [0], B => [1],C => [2]
        # length: len(string)
        #process to convert character to integer by ASCII is
        # reverse of Decode, but different function than chr()
        # (i.e., funtion to go from charater to number via ASCII)
        



    










        
