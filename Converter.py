#Converter class for Eng-Metric conversion by Meri Iskali

class Conversions:

    @staticmethod
    def MitoKi(mi):
        if not isinstance(mi,(int,float)):
            mi = float(mi)
        if mi < 0:
            raise ValueError("Error: negative values not legal for miles.")
        ki = mi * 1.60934
        return ki

    @staticmethod
    def OztoGr(oz):
        if not isinstance(oz,(int, float)):
            oz = float(oz)
        if oz < 0:
            raise ValueError("Error: negative values not legal for ounces.")
        gr = oz * 28.3495
        return gr

    @staticmethod
    def degreesK(c):
        if not isinstance(c,(int,float)):
            c = float(c)
        k = c + 273.15
        if c < 0:
            raise ValueError("temp not possible as it is below absolute zero.")
        return k

        
    @staticmethod
    def FtoC(f):
        if not isinstance(f,(int, float)):
            f = float(f)
        c = 5.0 / 9.0 * (f - 32)
        Conversions.degreesK(c)
        return c
    
    
    @staticmethod
    def CtoF(c):
        if not isinstance(c,(int, float)):
            c = float(c)
        f = 9.0 / 5.0 * c + 32.0
        Conversions.degreesK(c)
        return f



    @staticmethod
    def MetoFt(me):
        if not isinstance(me,(int, float)):
            me = float(me)
        if me < 0:
            raise ValueError("Error: negative values not legal for meters.")    
        ft = me * 3.2808
        return ft


    @staticmethod
    def LitoGal(li):
        if not isinstance(li,(int, float)):
            li = float(li)
        if li < 0:
            raise ValueError("Error: negative values not legal for litters.")   
        gal = li * .26417
        return gal


    
















    
