#Ninary to Decimal conversion from Meri Iskali

from Bin2Dec import Bin2Dec

def getChoice():
    c = - 1
    while c < 0 or c > 1:
        try:
            c = int(input("Binary Choice ? (1=Binary, 0=Quit): "))
            if c < 0 or c > 1:
                print("Unknown game type: 0 or 1 only.")
        except ValueError:
            print("Illegal input: intergers from 0 to 1 only")
            c = -1

    return c


def main():
    print("Welcome to the Binary-Decimal converter")

    choice = getChoice()
    while choice != 0:
        if choice == 1:
            self = input("Enter your binary value or quit to end: ")
            binary = Bin2Dec.getResultSteps(self)
            result = Bin2Dec.getResult(self)
            print("There is a " + str(binary) + " in the value.")
            print("Therefor the binary value: " + str(self) + "coverts to decimal"
                                                      + str(result))
            
        else:
            print("Thanks for using the Binary-Decimal Converter")
        print()
     



if __name__ =="__main__":
    main()
