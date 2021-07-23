#Conversion control program by Meri Iskali

from Converter import Conversions

def main():
    print("Welcome to the English-Metric Converter!\n")

    doK = False
    ans = input("On temp conversions do you want to see Kelvin? (Y/N): ")
    if len(ans) > 0 and ans[0].upper() == "Y":
        doK = True


    
    choice = getChoice()
    while choice != 0:
        try:
            if choice == 1:
                mi = getValue("Miles? ")
                ki = Conversions.MitoKi(mi)
                print(str(mi) + "Miles = " + str(round(ki,3)) + " Kilometers.")
            elif choice == 2:
                oz = getValue("Ounces? ")
                gr = Conversions.OztoGr(oz)
                print(str(oz) + " Ounces = " + str(round(gr,3)) + " grams.")
            elif choice == 3:
                f = getValue("Fahrenheit? ")
                c = Conversions.FtoC(f)
                print(str(f) + " Fahrenheit = " + str(round(c,3)) + " celcius.")
                if doK:
                    k = Conversions.degreesK(c)
                    print(" which is also a temp of " + str(round(k,3)) + " Kelvin.")
            elif choice == 4:
                c = getValue("Celsius? ")
                f = Conversions.CtoF(c)
                print(str(c) + " Celsius = " + str(round(f,3)) + " fahrenheit.")
                if doK:
                    k = Conversions.degreesK(c)
                    print(" which is also a temp of" + str(round(k,3)) + " Kelvin.")
            elif choice == 5:
                me = getValue("Meters? ")
                ft = Conversions.MetoFt(me)
                print(str(me) + " Meters =" + str(round(ft,3)) + " feet.")
            elif choice == 6:
                li = getValue("Liters? ")
                gal = Conversions.LitoGal(li)
                print(str(li) + " litters = " + str(round(gal, 3)) + " gallons.")
            else:
                print("Unknown conversion.")
            
        except ValueError as e:
            print("Data Problem: " + str(e))
        except Exception as e:
            print("General Error: " + str(e))     
        
        choice = getChoice()
        print("Thanks for using the converter!")
        print()

def getChoice():
    # must be completed; data validation and exception handling
    c = -1
    while c < 0 or c > 6:
        try:
            c = int(input("Conversion? (1=MitoKi, 2=OztoGr, 3=FtoC, 4=CtoF, 5=MtoFt, 6=LitoGal, 0=Quit): "))
            if c < 0 or c > 6:
                print("Uknown conversion of: 0, 1, 2, 3, 4, 5, or 6 only.")
        except ValueError:
            print("Illegal input: integers from 0 to 6 only")
            c = -1
    return c

def getValue(prompt):
    goodVal = False
    while not goodVal:
        try:
            val = float(input(prompt))
            goodVal = True
        except:
            print("Illegal value: numeric only please.")
            goodVal = False
    return val

if __name__=="__main__":
    main()
